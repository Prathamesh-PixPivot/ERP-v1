from rest_framework import serializers
from .models import (
    InventoryItem, InventoryItemVendor, InventorySerialNumber,
    WarehouseStock, CostingMethod, CycleCount, StockRecall,
    ShipmentTracking, VendorPerformance
)

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class InventoryItemVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItemVendor
        fields = '__all__'

class InventorySerialNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventorySerialNumber
        fields = '__all__'

class WarehouseStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseStock
        fields = '__all__'

class CostingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostingMethod
        fields = '__all__'

class CycleCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleCount
        fields = '__all__'

class StockRecallSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRecall
        fields = '__all__'

class ShipmentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentTracking
        fields = '__all__'

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPerformance
        fields = '__all__'
