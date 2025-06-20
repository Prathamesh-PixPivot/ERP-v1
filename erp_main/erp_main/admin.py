# erp_main/admin.py

from django.contrib import admin
from erp_main.models import TenantMetadata

admin.site.register(TenantMetadata)
