from rest_framework import serializers
from .models import (
    Vendor, VendorContact, VendorAddress, VendorRating, AutoPORequest,
    PurchaseOrder, Payment, Approval, Performance, VendorAudit,
    Inspection, VendorBlacklist
)

class VendorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorContact
        fields = '__all__'

class VendorAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAddress
        fields = '__all__'

class VendorRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorRating
        fields = '__all__'

class AutoPORequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoPORequest
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

class VendorAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAudit
        fields = '__all__'

class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'

class VendorBlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorBlacklist
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    contacts = VendorContactSerializer(many=True, read_only=True)
    addresses = VendorAddressSerializer(many=True, read_only=True)
    ratings = VendorRatingSerializer(many=True, read_only=True)
    auto_po_requests = AutoPORequestSerializer(many=True, read_only=True)
    purchase_orders = PurchaseOrderSerializer(many=True, read_only=True)
    performances = PerformanceSerializer(many=True, read_only=True)
    audits = VendorAuditSerializer(many=True, read_only=True)
    blacklists = VendorBlacklistSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = '__all__'
