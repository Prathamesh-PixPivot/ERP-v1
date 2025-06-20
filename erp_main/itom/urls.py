from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HostViewSet, ServiceViewSet, DashboardSummaryView


router = DefaultRouter()
router.register(r'hosts', HostViewSet)
router.register(r'services', ServiceViewSet)


urlpatterns = [
    path('dashboard/', DashboardSummaryView.as_view()),
    path('', include(router.urls)),
]
