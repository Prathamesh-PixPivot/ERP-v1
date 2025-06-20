from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import (
    CompanyDetail, IndividualContact, Lead, Opportunity,
    Proposal, Activity, Task, Meeting
)
from .serializers import (
    CompanyDetailSerializer, IndividualContactSerializer, LeadSerializer,
    OpportunitySerializer, ProposalSerializer, ActivitySerializer,
    TaskSerializer, MeetingSerializer
)

class CompanyDetailViewSet(viewsets.ModelViewSet):
    queryset = CompanyDetail.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = [IsAuthenticated]

class IndividualContactViewSet(viewsets.ModelViewSet):
    queryset = IndividualContact.objects.all()
    serializer_class = IndividualContactSerializer
    permission_classes = [IsAuthenticated]

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permission_classes = [IsAuthenticated]

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = [IsAuthenticated]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated]