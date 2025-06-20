from rest_framework import serializers
from .models import (
    CompanyDetail, IndividualContact, Lead, Opportunity,
    Proposal, Activity, Task, Meeting
)

class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetail
        fields = '__all__'

class IndividualContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualContact
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'