import json

from django.conf import settings
from django.core.cache import cache
import os
from django.core.management import call_command
from django.db import connections
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_tenant_database(db_name):
    conn = psycopg2.connect(
        dbname="mydb",
        user=os.environ.get("POSTGRES_USER", "tess"),
        password=os.environ.get("POSTGRES_PASSWORD", "pass"),
        host=os.environ.get("POSTGRES_HOST", "localhost"),
        port=os.environ.get("POSTGRES_PORT", "5433"),
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with conn.cursor() as cur:
        cur.execute(f"CREATE DATABASE {db_name};")
    conn.close()


def migrate_tenant_database(db_name):
    call_command("migrate", database=db_name)
    call_command("migrate", "token_blacklist", database=db_name)


def seed_tenant_database(db_name):
    fixtures_path = os.path.join("erp_main", "fixtures", "initial_data.json")
    if os.path.exists(fixtures_path):
        call_command("loaddata", fixtures_path, database=db_name)


def get_cached_db_config(tenant_db_name):
    key = f"tenant_db_config:{tenant_db_name}"
    cached = cache.get(key)
    if cached:
        return json.loads(cached)
    return None


def cache_db_config(tenant_db_name, config):
    key = f"tenant_db_config:{tenant_db_name}"
    cache.set(key, json.dumps(config), timeout=3600 * 24)  # Cache for 24 hours


def ensure_tenant_db_config(tenant_db_name: str):
    if tenant_db_name in settings.DATABASES:
        return

    cached_config = get_cached_db_config(tenant_db_name)
    if cached_config:
        # Ensure TIME_ZONE is injected
        cached_config.setdefault('TIME_ZONE', getattr(settings, 'TIME_ZONE', 'UTC'))
        settings.DATABASES[tenant_db_name] = cached_config
        return

    default = settings.DATABASES['default']

    config = {
        'ENGINE': default['ENGINE'],
        'NAME': tenant_db_name,
        'USER': default['USER'],
        'PASSWORD': default['PASSWORD'],
        'HOST': default['HOST'],
        'PORT': default['PORT'],
        'OPTIONS': default.get('OPTIONS', {}),
        'ATOMIC_REQUESTS': default.get('ATOMIC_REQUESTS', False),
        'CONN_MAX_AGE': default.get('CONN_MAX_AGE', 0),
        'TIME_ZONE': getattr(settings, 'TIME_ZONE', 'UTC'),  # ✅ must be present
        'DISABLE_SERVER_SIDE_CURSORS': default.get('DISABLE_SERVER_SIDE_CURSORS', False),
        'TEST': default.get('TEST', {}),
        'CONN_HEALTH_CHECKS': default.get('CONN_HEALTH_CHECKS', False),
        'AUTOCOMMIT': default.get('AUTOCOMMIT', True),
    }

    settings.DATABASES[tenant_db_name] = config
    cache_db_config(tenant_db_name, config)
