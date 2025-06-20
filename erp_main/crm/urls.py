from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyDetailViewSet, IndividualContactViewSet, LeadViewSet,
    OpportunityViewSet, ProposalViewSet, ActivityViewSet,
    TaskViewSet, MeetingViewSet
)

router = DefaultRouter()
router.register(r'companies', CompanyDetailViewSet)
router.register(r'contacts', IndividualContactViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'opportunities', OpportunityViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
