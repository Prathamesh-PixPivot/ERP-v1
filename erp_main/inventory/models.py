from django.db import models

class InventoryItem(models.Model):
    UNIT_CHOICES = [
        ('pcs', 'pcs'),
        ('kg', 'kg'),
        ('liters', 'liters')
    ]

    product_name = models.CharField(max_length=255)
    product_description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    available_quantity = models.IntegerField(default=0)
    reorder_point = models.IntegerField(default=0)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    batch_number = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    unit_of_measurement = models.CharField(max_length=50, choices=UNIT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InventoryItemVendor(models.Model):
    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    vendor_id = models.CharField(max_length=64)

    class Meta:
        unique_together = ('product', 'vendor_id')

class InventorySerialNumber(models.Model):
    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100)

    class Meta:
        unique_together = ('product', 'serial_number')

class WarehouseStock(models.Model):
    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    warehouse_id = models.CharField(max_length=64)
    location_id = models.CharField(max_length=64)
    stock_level = models.IntegerField(default=0)
    reserved_quantity = models.IntegerField(default=0)

class CostingMethod(models.Model):
    COSTING_CHOICES = [
        ('FIFO', 'FIFO'),
        ('LIFO', 'LIFO'),
        ('Weighted Average', 'Weighted Average')
    ]
    costing_method = models.CharField(max_length=50, choices=COSTING_CHOICES)
    applied_at = models.DateTimeField(auto_now_add=True)

class CycleCount(models.Model):
    warehouse_id = models.CharField(max_length=64)
    success = models.BooleanField(default=False)
    report_link = models.TextField(blank=True, null=True)
    performed_at = models.DateTimeField(auto_now_add=True)

class StockRecall(models.Model):
    product = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    reason = models.TextField()
    success = models.BooleanField(default=False)
    recalled_at = models.DateTimeField(auto_now_add=True)

class ShipmentTracking(models.Model):
    tracking_number = models.CharField(max_length=100)
    carrier_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class VendorPerformance(models.Model):
    on_time_delivery_rate = models.FloatField()
    defect_rate = models.FloatField()
