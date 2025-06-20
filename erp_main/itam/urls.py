from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    AssetViewSet, AllocationViewSet, AuditViewSet,
    LicenseViewSet, DisposalViewSet, MaintenanceViewSet
)

router = DefaultRouter()
router.register(r'assets', AssetViewSet)
router.register(r'allocations', AllocationViewSet)
router.register(r'audits', AuditViewSet)
router.register(r'licenses', LicenseViewSet)
router.register(r'disposals', DisposalViewSet)
router.register(r'maintenances', MaintenanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]