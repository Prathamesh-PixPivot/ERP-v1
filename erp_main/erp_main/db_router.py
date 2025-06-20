from django.db import connections
from erp_main.middleware import get_current_tenant


class TenantRouter:
    """
    A database router that directs database operations to the appropriate
    tenant-specific database, based on the current request context.
    """

    def db_for_read(self, model, **hints):
        """
        Route read operations to the tenant-specific database.
        """
        if model._meta.app_label == 'erp_main' and model.__name__ == 'TenantMetadata':
            return 'default'
        return hints.get('tenant_db') or get_current_tenant()

    def db_for_write(self, model, **hints):
        """
        Route write operations to the tenant-specific database.
        """
        return hints.get('tenant_db') or self._get_dynamic_db()

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow any relation between objects (cross-db allowed).
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations on the default DB and tenant databases prefixed with 'tenant_'.
        """
        return db == 'default' or db.startswith('tenant_')

    def _get_dynamic_db(self):
        """
        Returns the current tenant's DB name using context-local thread storage.
        Falls back to 'default' if not found.
        """
        try:
            tenant_db = get_current_tenant()
            return tenant_db or 'default'
        except Exception:
            return 'default'
