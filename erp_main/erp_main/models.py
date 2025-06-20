# erp_main/models.py

from django.db import models

class TenantMetadata(models.Model):
    org_name = models.CharField(max_length=255, unique=True)
    db_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name
