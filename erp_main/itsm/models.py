from django.db import models


class Incident(models.Model):
    """Basic incident record created from monitoring alerts."""

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, default="new")
    zabbix_event_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "itsm_incidents"

    def __str__(self) -> str:
        return self.title
