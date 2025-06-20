from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    InventoryItem, InventoryItemVendor, InventorySerialNumber,
    WarehouseStock, CostingMethod, CycleCount, StockRecall,
    ShipmentTracking, VendorPerformance
)
from .serializers import (
    InventoryItemSerializer, InventoryItemVendorSerializer, InventorySerialNumberSerializer,
    WarehouseStockSerializer, CostingMethodSerializer, CycleCountSerializer,
    StockRecallSerializer, ShipmentTrackingSerializer, VendorPerformanceSerializer
)

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

class InventoryItemVendorViewSet(viewsets.ModelViewSet):
    queryset = InventoryItemVendor.objects.all()
    serializer_class = InventoryItemVendorSerializer
    permission_classes = [IsAuthenticated]

class InventorySerialNumberViewSet(viewsets.ModelViewSet):
    queryset = InventorySerialNumber.objects.all()
    serializer_class = InventorySerialNumberSerializer
    permission_classes = [IsAuthenticated]

class WarehouseStockViewSet(viewsets.ModelViewSet):
    queryset = WarehouseStock.objects.all()
    serializer_class = WarehouseStockSerializer
    permission_classes = [IsAuthenticated]

class CostingMethodViewSet(viewsets.ModelViewSet):
    queryset = CostingMethod.objects.all()
    serializer_class = CostingMethodSerializer
    permission_classes = [IsAuthenticated]

class CycleCountViewSet(viewsets.ModelViewSet):
    queryset = CycleCount.objects.all()
    serializer_class = CycleCountSerializer
    permission_classes = [IsAuthenticated]

class StockRecallViewSet(viewsets.ModelViewSet):
    queryset = StockRecall.objects.all()
    serializer_class = StockRecallSerializer
    permission_classes = [IsAuthenticated]

class ShipmentTrackingViewSet(viewsets.ModelViewSet):
    queryset = ShipmentTracking.objects.all()
    serializer_class = ShipmentTrackingSerializer
    permission_classes = [IsAuthenticated]

class VendorPerformanceViewSet(viewsets.ModelViewSet):
    queryset = VendorPerformance.objects.all()
    serializer_class = VendorPerformanceSerializer
    permission_classes = [IsAuthenticated]
