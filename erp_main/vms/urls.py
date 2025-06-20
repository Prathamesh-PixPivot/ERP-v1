from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'vendor-contacts', VendorContactViewSet)
router.register(r'vendor-addresses', VendorAddressViewSet)
router.register(r'vendor-ratings', VendorRatingViewSet)
router.register(r'auto-po-requests', AutoPORequestViewSet)
router.register(r'purchase-orders', PurchaseOrderViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'approvals', ApprovalViewSet)
router.register(r'vendor-performances', PerformanceViewSet)
router.register(r'vendor-audits', VendorAuditViewSet)
router.register(r'inspections', InspectionViewSet)
router.register(r'vendor-blacklists', VendorBlacklistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
