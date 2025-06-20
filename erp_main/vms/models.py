from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    gstin = models.CharField(max_length=255)
    certifications = models.TextField()
    licenses = models.TextField()
    is_compliant = models.BooleanField(default=False)
    performance_score = models.FloatField()
    risk_assessment = models.TextField()

class VendorContact(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=50)

class VendorAddress(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='addresses')
    address_line1 = models.TextField()
    address_line2 = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

class VendorRating(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='ratings')
    rating = models.FloatField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class AutoPORequest(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='auto_po_requests')
    success = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_number = models.CharField(max_length=100)
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=100)
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='payments')
    amount = models.FloatField()
    status = models.CharField(max_length=100)
    payment_terms = models.TextField()
    paid_at = models.DateTimeField(null=True, blank=True)

class Approval(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='approvals')
    approver_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    approved_at = models.DateTimeField(null=True, blank=True)
    comments = models.TextField()

class Performance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='performances')
    metric_name = models.CharField(max_length=100)
    metric_value = models.FloatField()
    recorded_at = models.DateTimeField()

class VendorAudit(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='audits')
    audit_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Inspection(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='inspections')
    inspection_notes = models.TextField()
    success = models.BooleanField()
    inspected_at = models.DateTimeField(auto_now_add=True)

class VendorBlacklist(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='blacklists')
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
