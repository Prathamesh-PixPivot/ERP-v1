from tokenize import TokenError

from django.db import connections, OperationalError
from django.db import transaction
from django_ratelimit.decorators import ratelimit
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from erp_main.models import TenantMetadata
from erp_main.utils.db_utils import ensure_tenant_db_config, migrate_tenant_database, seed_tenant_database, \
    create_tenant_database
from .models import User, Organization
from .serializers import RegisterSerializer, UserSerializer, OrganizationSerializer
from .utils import migrate_token_blacklist_if_missing


@ratelimit(key='ip', rate='5/m', block=True)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    data = request.data
    org_data = data.get('organization', {})
    user_data = {k: v for k, v in data.items() if k != 'organization'}

    org_name = org_data.get('name')
    user_email = user_data.get('email')

    if not org_name or not user_email:
        return Response({'error': 'Organization name and user email are required.'}, status=400)

    tenant_db_name = f"tenant_{org_name.lower().replace(' ', '_')}"

    # Step 1: Check if tenant DB exists
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", [tenant_db_name])
            db_exists = bool(cursor.fetchone())
    except OperationalError as e:
        return Response({'error': f'Failed to query public DB: {e}'}, status=500)

    # Step 2: Register DB config
    ensure_tenant_db_config(tenant_db_name)

    try:
        if db_exists:
            # Check if initial tables exist
            with connections[tenant_db_name].cursor() as cursor:
                cursor.execute("SELECT to_regclass('public.user_auth_user');")
                user_table_exists = cursor.fetchone()[0] is not None

            if not user_table_exists:
                migrate_tenant_database(tenant_db_name)
                seed_tenant_database(tenant_db_name)

            migrate_token_blacklist_if_missing(tenant_db_name)

            if User.objects.using(tenant_db_name).filter(email=user_email).exists():
                return Response({'error': 'User already registered in this tenant.'}, status=400)

        else:
            # New DB provisioning
            create_tenant_database(tenant_db_name)
            migrate_tenant_database(tenant_db_name)
            seed_tenant_database(tenant_db_name)
            migrate_token_blacklist_if_missing(tenant_db_name)

    except Exception as e:
        return Response({'error': f'Tenant DB setup failed: {e}'}, status=500)

    # Step 3: Validate payload
    serializer = RegisterSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    validated = serializer.validated_data
    org_payload = validated.pop('organization')

    try:
        with transaction.atomic(using=tenant_db_name):
            org = Organization.objects.using(tenant_db_name).create(**org_payload)
            user = User.objects.using(tenant_db_name).create(organization=org, **validated)
            user.set_password(validated['password'])
            user.save(using=tenant_db_name)
    except Exception as e:
        return Response({'error': f'Failed to create tenant user/org: {e}'}, status=500)

    TenantMetadata.objects.update_or_create(
        email=user_email,
        defaults={'org_name': org_name, 'db_name': tenant_db_name}
    )

    return Response(UserSerializer(user).data, status=201)

@ratelimit(key='ip', rate='5/m', block=True)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_jwt_view(request):
    from django.contrib.auth import get_user_model
    from erp_main.models import TenantMetadata
    from erp_main.utils.db_utils import ensure_tenant_db_config
    from user_auth.utils import generate_tenant_jwt

    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Missing email or password.'}, status=400)

    try:
        tenant = TenantMetadata.objects.using('default').get(email=email)
    except TenantMetadata.DoesNotExist:
        return Response({'error': 'Tenant not found.'}, status=404)

    tenant_db = tenant.db_name
    ensure_tenant_db_config(tenant_db)
    User = get_user_model()

    try:
        user = User.objects.using(tenant_db).get(email=email)
        if user.check_password(password):
            tokens = generate_tenant_jwt(user, tenant_db)
            return Response({
                "access": tokens["access"],
                "refresh": tokens["refresh"],
                "tenant": tenant_db,
                "message": "Login successful"
            })
        else:
            return Response({'error': 'Invalid credentials.'}, status=400)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials.'}, status=400)


@ratelimit(key='ip', rate='5/m', block=True)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    tenant_db = getattr(request, 'tenant_db', None) or request.session.get('tenant_db')
    if not tenant_db:
        return Response({'error': 'Missing tenant context'}, status=400)

    ensure_tenant_db_config(tenant_db)
    return Response(UserSerializer(request.user).data)

@ratelimit(key='ip', rate='5/m', block=True)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_jwt_view(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        # ✅ Also blacklist the current access token
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            access_token = auth_header.split()[1]
            from rest_framework_simplejwt.tokens import AccessToken
            access_obj = AccessToken(access_token)
            jti = access_obj['jti']
            try:
                ot = OutstandingToken.objects.get(jti=jti)
                BlacklistedToken.objects.get_or_create(token=ot)
            except OutstandingToken.DoesNotExist:
                pass

        return Response({"detail": "Logged out"}, status=205)
    except (TokenError, KeyError):
        return Response({"error": "Invalid token"}, status=400)


@ratelimit(key='ip', rate='5/m', block=True)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_organization(request):
    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
        org = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@ratelimit(key='ip', rate='5/m', block=True)
@api_view(['GET'])
@permission_classes([AllowAny])
def list_organizations(request):
    orgs = Organization.objects.all()
    serializer = OrganizationSerializer(orgs, many=True)
    return Response(serializer.data)

class TenantTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = request.data.get('refresh')

        try:
            token = RefreshToken(refresh_token)
            tenant_db = token.get("tenant")
            if tenant_db:
                new_access_token = response.data["access"]
                decoded = RefreshToken(new_access_token)
                decoded["tenant"] = tenant_db
                response.data["access"] = str(decoded)
        except Exception:
            raise InvalidToken("Invalid refresh token")

        return response