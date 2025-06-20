# user_auth/utils.py
from datetime import datetime, timezone

from django.core.management import call_command
from django.db import connections
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

def generate_tenant_jwt(user, tenant_db):
    refresh = RefreshToken.for_user(user)
    refresh["tenant"] = tenant_db

    access_token = refresh.access_token
    access_token["tenant"] = tenant_db

    # ✅ Manually register access token in OutstandingToken
    OutstandingToken.objects.get_or_create(
        user=user,
        jti=access_token["jti"],
        token=str(access_token),
        created_at=datetime.now(timezone.utc),
        expires_at=datetime.fromtimestamp(access_token['exp'], tz=timezone.utc)
    )

    return {
        'refresh': str(refresh),
        'access': str(access_token),
    }

def migrate_token_blacklist_if_missing(tenant_db_name: str):
    with connections[tenant_db_name].cursor() as cursor:
        cursor.execute("SELECT to_regclass('token_blacklist_outstandingtoken');")
        exists = cursor.fetchone()[0] is not None

    if not exists:
        call_command('migrate', 'token_blacklist', database=tenant_db_name)