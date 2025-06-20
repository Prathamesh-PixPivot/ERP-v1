from django.db import models
from decimal import Decimal
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=255)
    hsn_code = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=50, blank=True)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name

class BaseDocument(models.Model):
    DRAFT = 'draft'
    SENT = 'sent'
    APPROVED = 'approved'
    PAID = 'paid'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (SENT, 'Sent'),
        (APPROVED, 'Approved'),
        (PAID, 'Paid'),
        (CANCELLED, 'Cancelled'),
    ]

    reference_number = models.CharField(max_length=100, unique=True)
    date = models.DateField(default=timezone.now)
    currency = models.CharField(max_length=10, default='INR')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    terms_and_conditions = models.TextField(blank=True)

    items = models.ManyToManyField(Item, blank=True)

    class Meta:
        abstract = True

class Quotation(BaseDocument):
    customer_name = models.CharField(max_length=255)
    valid_until = models.DateField(null=True, blank=True)
    billing_address = models.TextField(blank=True)
    shipping_address = models.TextField(blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Quotation {self.reference_number} for {self.customer_name}"

class ProformaInvoice(BaseDocument):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name='proforma_invoices')
    valid_until = models.DateField(null=True, blank=True)
    billing_address = models.TextField(blank=True)
    shipping_address = models.TextField(blank=True)

    def __str__(self):
        return f"ProformaInvoice {self.reference_number} from Quotation {self.quotation.reference_number}"

class SalesInvoice(BaseDocument):
    proforma_invoice = models.ForeignKey(ProformaInvoice, on_delete=models.CASCADE, related_name='sales_invoices')
    payment_due_date = models.DateField(null=True, blank=True)
    billing_address = models.TextField(blank=True)
    shipping_address = models.TextField(blank=True)
    payment_terms = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"SalesInvoice {self.reference_number} from Proforma {self.proforma_invoice.reference_number}"

class EWayBill(models.Model):
    sales_invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE, related_name='eway_bills')
    bill_number = models.CharField(max_length=100, unique=True)
    transport_mode = models.CharField(max_length=50, blank=True)
    vehicle_number = models.CharField(max_length=100, blank=True)
    transporter_name = models.CharField(max_length=255, blank=True)
    origin_address = models.TextField(blank=True)
    destination_address = models.TextField(blank=True)
    distance_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    estimated_delivery_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"EWayBill {self.bill_number} for Invoice {self.sales_invoice.reference_number}"

class PurchaseInvoice(BaseDocument):
    supplier_name = models.CharField(max_length=255)
    payment_due_date = models.DateField(null=True, blank=True)
    billing_address = models.TextField(blank=True)
    payment_terms = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"PurchaseInvoice {self.reference_number} for {self.supplier_name}"


class Ledger(models.Model):
    entry_id = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    debit = models.FloatField(default=0.0)
    credit = models.FloatField(default=0.0)
    opening_balance = models.FloatField(default=0.0)
    closing_balance = models.FloatField(default=0.0)
    transaction_date = models.DateTimeField()

    def __str__(self):
        return f"{self.entry_id} | {self.transaction_date}"

    def save(self, *args, **kwargs):
        if not self.pk:
            prev = Ledger.objects.filter(transaction_date__lt=self.transaction_date).order_by('-transaction_date').first()
            ob = prev.closing_balance if prev else 0.0
        else:
            ob = self.opening_balance
        self.opening_balance = ob
        self.closing_balance = ob + self.debit - self.credit
        super().save(*args, **kwargs)


class BaseNote(models.Model):
    note_id = models.CharField(max_length=100, unique=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CreditNote(BaseNote):
    sales_invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE)

class DebitNote(BaseNote):
    purchase_invoice = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE)
