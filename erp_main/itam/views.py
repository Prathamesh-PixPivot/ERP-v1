from rest_framework import viewsets
from .models import Asset, Allocation, Audit, License, Disposal, Maintenance
from .serializers import (
    AssetSerializer, AllocationSerializer, AuditSerializer,
    LicenseSerializer, DisposalSerializer, MaintenanceSerializer
)

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AllocationViewSet(viewsets.ModelViewSet):
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer

class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class DisposalViewSet(viewsets.ModelViewSet):
    queryset = Disposal.objects.all()
    serializer_class = DisposalSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
