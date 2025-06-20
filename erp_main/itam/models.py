from django.db import models
import uuid

class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, db_index=True)
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
    current_value = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=[
            ('active', 'Active'),
            ('allocated', 'Allocated'),
            ('under_maintenance', 'Under Maintenance'),
            ('disposed', 'Disposed'),
        ],
        db_index=True
    )
    depreciation_rate = models.DecimalField(max_digits=5, decimal_places=4)
    guidelines = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['category']), models.Index(fields=['status'])]
        ordering = ['-purchase_date']
        verbose_name_plural = 'Assets'

    def __str__(self):
        return f"{self.name} ({self.id})"

class Allocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, related_name='allocations', on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=255)
    assignment_date = models.DateTimeField()
    release_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['asset'])]
        ordering = ['-assignment_date']
        verbose_name_plural = 'Allocations'



class Audit(models.Model):
    id = models.AutoField(primary_key=True)
    asset = models.ForeignKey(Asset, related_name='audits', on_delete=models.CASCADE)
    audited_by = models.CharField(max_length=255)
    condition = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)
    audit_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['asset'])]
        ordering = ['-audit_date']
        verbose_name_plural = 'Audits'

    def __str__(self):
        return f"Audit {self.id} on {self.audit_date.date()}"

class License(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, related_name='licenses', on_delete=models.CASCADE)
    license_key = models.CharField(max_length=255)
    expiry_date = models.DateField()
    vendor = models.CharField(max_length=255)
    contract_details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['asset'])]
        ordering = ['expiry_date']
        verbose_name_plural = 'Licenses'



class Disposal(models.Model):
    id = models.AutoField(primary_key=True)
    asset = models.OneToOneField(Asset, related_name='disposal', on_delete=models.CASCADE)
    reason = models.TextField()
    decommission_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Disposals'



class Maintenance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, related_name='maintenances', on_delete=models.CASCADE)
    maintenance_date = models.DateTimeField()
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['asset'])]
        ordering = ['-maintenance_date']
        verbose_name_plural = 'Maintenances'

    def __str__(self):
        return f"Maintenance {self.id} on {self.maintenance_date.date()}"
