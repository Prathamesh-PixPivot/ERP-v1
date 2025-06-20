from rest_framework import serializers
from .models import Asset, Allocation, Audit, License, Disposal, Maintenance

class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocation
        fields = '__all__'

class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit
        fields = '__all__'

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'

class DisposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disposal
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    allocations = AllocationSerializer(many=True, read_only=True)
    audits = AuditSerializer(many=True, read_only=True)
    licenses = LicenseSerializer(many=True, read_only=True)
    maintenances = MaintenanceSerializer(many=True, read_only=True)
    disposal = DisposalSerializer(read_only=True)

    class Meta:
        model = Asset
        fields = [
            'id', 'name', 'description', 'category', 'purchase_date', 'purchase_price',
            'current_value', 'location', 'status', 'depreciation_rate', 'guidelines',
            'created_at', 'updated_at', 'deleted_at',
            'allocations', 'audits', 'licenses', 'maintenances', 'disposal'
        ]

