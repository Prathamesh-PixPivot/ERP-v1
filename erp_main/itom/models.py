from django.db import models


class Host(models.Model):
    """A monitored host."""

    name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    zabbix_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'itom_hosts'

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    """A service running on a host."""

    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=255)
    port = models.PositiveIntegerField()
    zabbix_service_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'itom_services'

    def __str__(self) -> str:
        return f"{self.name} ({self.port})"
