from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ItemViewSet, QuotationViewSet, ProformaInvoiceViewSet,
    SalesInvoiceViewSet, EWayBillViewSet, PurchaseInvoiceViewSet,
    LedgerViewSet, CreditNoteViewSet, DebitNoteViewSet
)

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'quotations', QuotationViewSet)
router.register(r'proforma-invoices', ProformaInvoiceViewSet)
router.register(r'sales-invoices', SalesInvoiceViewSet)
router.register(r'eway-bills', EWayBillViewSet)
router.register(r'purchase-invoices', PurchaseInvoiceViewSet)
router.register(r'ledgers', LedgerViewSet)
router.register(r'credit-notes', CreditNoteViewSet)
router.register(r'debit-notes', DebitNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
