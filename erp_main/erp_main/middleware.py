import threading
from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from erp_main.utils.db_utils import ensure_tenant_db_config
from erp_main.utils.tenant_cache import get_tenant_metadata_cached

_thread_locals = threading.local()

def get_current_tenant():
    return getattr(_thread_locals, 'tenant_db', 'default')


class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tenant_db = None

        # STEP 1: JWT-Based Resolution
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            try:
                jwt_auth = JWTAuthentication()
                token = jwt_auth.get_raw_token(auth_header)
                validated = jwt_auth.get_validated_token(token)
                tenant_db = validated.get('tenant')

                if tenant_db:
                    ensure_tenant_db_config(tenant_db)
                    request.tenant_db = tenant_db
                    from user_auth.auth import TenantJWTAuthentication
                    user_auth = TenantJWTAuthentication()
                    user, _ = user_auth.authenticate(request)
                    request.user = user

            except Exception:
                pass  # fallback to subdomain

        # STEP 2: Subdomain fallback
        if not tenant_db:
            host = request.get_host().split(':')[0]
            domain_parts = host.split('.')
            subdomain = None

            if host.endswith(('lvh.me', 'nip.io')) and len(domain_parts) >= 3:
                subdomain = domain_parts[0]
            elif len(domain_parts) >= 3:
                subdomain = domain_parts[0]

            if subdomain:
                tenant_info = get_tenant_metadata_cached(subdomain)
                if tenant_info:
                    tenant_db = tenant_info.get('db_name')
                else:
                    return HttpResponseBadRequest(f"Unknown tenant: {subdomain}")

        if not tenant_db:
            tenant_db = 'default'

        ensure_tenant_db_config(tenant_db)
        _thread_locals.tenant_db = tenant_db
        request.tenant_db = tenant_db
