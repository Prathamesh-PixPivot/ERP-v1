from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Host, Service
from .serializers import HostSerializer, ServiceSerializer
from .zabbix_client import ZabbixClient


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        client = ZabbixClient()
        try:
            result = client.create_host(instance.name, instance.ip_address)
            instance.zabbix_id = result.get('hostids', [None])[0]
            instance.save(update_fields=['zabbix_id'])
        except Exception:
            pass


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class DashboardSummaryView(APIView):
    """Return basic host summary from Zabbix."""

    def get(self, request):
        client = ZabbixClient()
        data = client.host_status_summary()
        return Response({"hosts": data})

