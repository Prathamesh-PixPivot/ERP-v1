from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InventoryItemViewSet, InventoryItemVendorViewSet, InventorySerialNumberViewSet,
    WarehouseStockViewSet, CostingMethodViewSet, CycleCountViewSet,
    StockRecallViewSet, ShipmentTrackingViewSet, VendorPerformanceViewSet
)

router = DefaultRouter()
router.register(r'inventory-items', InventoryItemViewSet)
router.register(r'vendors', InventoryItemVendorViewSet)
router.register(r'serial-numbers', InventorySerialNumberViewSet)
router.register(r'warehouse-stocks', WarehouseStockViewSet)
router.register(r'costing-methods', CostingMethodViewSet)
router.register(r'cycle-counts', CycleCountViewSet)
router.register(r'stock-recalls', StockRecallViewSet)
router.register(r'shipment-trackings', ShipmentTrackingViewSet)
router.register(r'vendor-performances', VendorPerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
