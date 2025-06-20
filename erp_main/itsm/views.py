from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Incident
from .serializers import IncidentSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class ZabbixWebhookView(APIView):
    """Endpoint for Zabbix to create an Incident."""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        payload = request.data or {}
        event = payload.get("event", {})
        incident = Incident.objects.create(
            title=event.get("name", "Zabbix event"),
            description=event.get("description", ""),
            zabbix_event_id=event.get("id"),
        )
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)
