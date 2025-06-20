from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import (
    Item, Quotation, ProformaInvoice, SalesInvoice, EWayBill,
    PurchaseInvoice, Ledger, CreditNote, DebitNote
)
from .serializers import (
    ItemSerializer, QuotationSerializer, ProformaInvoiceSerializer,
    SalesInvoiceSerializer, EWayBillSerializer, PurchaseInvoiceSerializer,
    LedgerSerializer, CreditNoteSerializer, DebitNoteSerializer
)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer
    permission_classes = [IsAuthenticated]

class ProformaInvoiceViewSet(viewsets.ModelViewSet):
    queryset = ProformaInvoice.objects.all()
    serializer_class = ProformaInvoiceSerializer
    permission_classes = [IsAuthenticated]

class SalesInvoiceViewSet(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer
    permission_classes = [IsAuthenticated]

class EWayBillViewSet(viewsets.ModelViewSet):
    queryset = EWayBill.objects.all()
    serializer_class = EWayBillSerializer
    permission_classes = [IsAuthenticated]

class PurchaseInvoiceViewSet(viewsets.ModelViewSet):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer
    permission_classes = [IsAuthenticated]

class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
    permission_classes = [IsAuthenticated]

class CreditNoteViewSet(viewsets.ModelViewSet):
    queryset = CreditNote.objects.all()
    serializer_class = CreditNoteSerializer
    permission_classes = [IsAuthenticated]

class DebitNoteViewSet(viewsets.ModelViewSet):
    queryset = DebitNote.objects.all()
    serializer_class = DebitNoteSerializer
    permission_classes = [IsAuthenticated]
