from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IncidentViewSet, ZabbixWebhookView


router = DefaultRouter()
router.register(r'incidents', IncidentViewSet)


urlpatterns = [
    path('zabbix/', ZabbixWebhookView.as_view()),
    path('', include(router.urls)),
]
