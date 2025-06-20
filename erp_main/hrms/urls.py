from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'designations', DesignationViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'bonus', BonusViewSet)
router.register(r'compliance', ComplianceRecordViewSet)
router.register(r'benefits', EmployeeBenefitViewSet)
router.register(r'documents', EmployeeDocumentViewSet)
router.register(r'exits', EmployeeExitViewSet)
router.register(r'perks', EmployeePerkViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'grievances', GrievanceViewSet)
router.register(r'reports', AnalyticsReportViewSet)
router.register(r'leavetypes', LeaveTypeViewSet)
router.register(r'leavepolicies', LeavePolicyViewSet)
router.register(r'leavebalances', LeaveBalanceViewSet)
router.register(r'leavetransactions', LeaveTransactionViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'publicholidays', PublicHolidayViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applicants', ApplicantViewSet)
router.register(r'interviews', InterviewViewSet)
router.register(r'onboardings', OnboardingViewSet)
router.register(r'shifts', ShiftViewSet)
router.register(r'salarystructures', SalaryStructureViewSet)
router.register(r'payrolls', PayrollViewSet)
router.register(r'loanadvances', LoanAdvanceViewSet)
router.register(r'performancereviews', PerformanceReviewViewSet)
router.register(r'skilldevelopments', SkillDevelopmentViewSet)
router.register(r'performancekpis', PerformanceKPIViewSet)
router.register(r'workhistories', WorkHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
