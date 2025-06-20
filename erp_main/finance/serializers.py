from rest_framework import serializers
from .models import (
    Item, Quotation, ProformaInvoice, SalesInvoice, EWayBill,
    PurchaseInvoice, Ledger, CreditNote, DebitNote
)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'

class ProformaInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProformaInvoice
        fields = '__all__'

class SalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = '__all__'

class EWayBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EWayBill
        fields = '__all__'

class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = '__all__'

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'

class CreditNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditNote
        fields = '__all__'

class DebitNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitNote
        fields = '__all__'
