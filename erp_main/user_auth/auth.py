from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

from erp_main.utils.db_utils import ensure_tenant_db_config
from erp_main.utils.tenant_cache import get_subdomain


class TenantJWTAuthentication(JWTAuthentication):
    def __init__(self, *args, **kwargs):
        print("🚀 TenantJWTAuthentication loaded")
        super().__init__(*args, **kwargs)

    def process_request(self, request):
        print("🔍 COOKIES:", request.COOKIES)
        print("🔍 HEADERS:", request.headers)

    def authenticate(self, request):
        print("🍪 COOKIES:", request.COOKIES)
        print("📬 HEADERS:", request.headers)
        self.request = request
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        # ✅ ENFORCE: Check if this access token is blacklisted
        jti = validated_token.get('jti')
        if jti and BlacklistedToken.objects.filter(token__jti=jti).exists():
            raise AuthenticationFailed("Token is blacklisted")

        tenant_db = validated_token.get("tenant")
        if not tenant_db:
            raise AuthenticationFailed("Missing tenant in token.")

        # Step 1: Match subdomain against token
        subdomain = get_subdomain(request)
        expected = f"tenant_{subdomain}"
        if tenant_db != expected:
            raise AuthenticationFailed("Token tenant mismatch with request subdomain.")

        ensure_tenant_db_config(tenant_db)
        request.tenant_db = tenant_db

        user = self.get_user(validated_token)
        return (user, validated_token)

    def get_raw_token(self, header):
        token = None
        if header is not None:
            token = super().get_raw_token(header)
        if not token:
            token = self.request.COOKIES.get("access")
        print("🔍 Got token:", token)
        return token
