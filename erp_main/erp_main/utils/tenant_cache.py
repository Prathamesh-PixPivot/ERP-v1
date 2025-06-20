import json
from django.core.cache import cache
from erp_main.models import TenantMetadata

def get_tenant_metadata_cached(subdomain: str):
    key = f"tenant_meta:{subdomain.lower()}"
    cached = cache.get(key)
    if cached:
        return json.loads(cached)

    try:
        tenant = TenantMetadata.objects.using('default').get(org_name__iexact=subdomain)
        data = {
            "org_name": tenant.org_name,
            "db_name": tenant.db_name,
            "email": tenant.email,
        }
        cache.set(key, json.dumps(data), timeout=86400)  # cache 24h
        return data
    except TenantMetadata.DoesNotExist:
        return None

from django.http import HttpRequest

def get_subdomain(request: HttpRequest) -> str:
    host = request.get_host().split(':')[0]
    parts = host.split('.')
    if host.endswith(('lvh.me', 'nip.io')) and len(parts) >= 3:
        return parts[0]
    elif len(parts) >= 3:
        return parts[0]
    return 'default'
