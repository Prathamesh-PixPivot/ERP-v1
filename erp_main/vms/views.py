from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

class VendorContactViewSet(viewsets.ModelViewSet):
    queryset = VendorContact.objects.all()
    serializer_class = VendorContactSerializer
    permission_classes = [IsAuthenticated]

class VendorAddressViewSet(viewsets.ModelViewSet):
    queryset = VendorAddress.objects.all()
    serializer_class = VendorAddressSerializer
    permission_classes = [IsAuthenticated]

class VendorRatingViewSet(viewsets.ModelViewSet):
    queryset = VendorRating.objects.all()
    serializer_class = VendorRatingSerializer
    permission_classes = [IsAuthenticated]

class AutoPORequestViewSet(viewsets.ModelViewSet):
    queryset = AutoPORequest.objects.all()
    serializer_class = AutoPORequestSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = [IsAuthenticated]

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]

class VendorAuditViewSet(viewsets.ModelViewSet):
    queryset = VendorAudit.objects.all()
    serializer_class = VendorAuditSerializer
    permission_classes = [IsAuthenticated]

class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
    permission_classes = [IsAuthenticated]

class VendorBlacklistViewSet(viewsets.ModelViewSet):
    queryset = VendorBlacklist.objects.all()
    serializer_class = VendorBlacklistSerializer
    permission_classes = [IsAuthenticated]
