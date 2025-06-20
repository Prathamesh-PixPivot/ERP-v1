from rest_framework import viewsets
from .models import *
from .serializers import *

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class BonusViewSet(viewsets.ModelViewSet):
    queryset = Bonus.objects.all()
    serializer_class = BonusSerializer

class ComplianceRecordViewSet(viewsets.ModelViewSet):
    queryset = ComplianceRecord.objects.all()
    serializer_class = ComplianceRecordSerializer

class EmployeeBenefitViewSet(viewsets.ModelViewSet):
    queryset = EmployeeBenefit.objects.all()
    serializer_class = EmployeeBenefitSerializer

class EmployeeDocumentViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer

class EmployeeExitViewSet(viewsets.ModelViewSet):
    queryset = EmployeeExit.objects.all()
    serializer_class = EmployeeExitSerializer

class EmployeePerkViewSet(viewsets.ModelViewSet):
    queryset = EmployeePerk.objects.all()
    serializer_class = EmployeePerkSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class GrievanceViewSet(viewsets.ModelViewSet):
    queryset = Grievance.objects.all()
    serializer_class = GrievanceSerializer

class AnalyticsReportViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsReport.objects.all()
    serializer_class = AnalyticsReportSerializer

from .models import (
    LeaveType, LeavePolicy, LeaveBalance, LeaveTransaction,
    Organization, PublicHoliday, Job, Applicant, Interview,
    Onboarding, Shift, SalaryStructure, Payroll, LoanAdvance,
    PerformanceReview, SkillDevelopment, PerformanceKPI, WorkHistory
)
from .serializers import (
    LeaveTypeSerializer, LeavePolicySerializer, LeaveBalanceSerializer, LeaveTransactionSerializer,
    OrganizationSerializer, PublicHolidaySerializer, JobSerializer, ApplicantSerializer, InterviewSerializer,
    OnboardingSerializer, ShiftSerializer, SalaryStructureSerializer, PayrollSerializer, LoanAdvanceSerializer,
    PerformanceReviewSerializer, SkillDevelopmentSerializer, PerformanceKPISerializer, WorkHistorySerializer
)

class LeaveTypeViewSet(viewsets.ModelViewSet):
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer

class LeavePolicyViewSet(viewsets.ModelViewSet):
    queryset = LeavePolicy.objects.all()
    serializer_class = LeavePolicySerializer

class LeaveBalanceViewSet(viewsets.ModelViewSet):
    queryset = LeaveBalance.objects.all()
    serializer_class = LeaveBalanceSerializer

class LeaveTransactionViewSet(viewsets.ModelViewSet):
    queryset = LeaveTransaction.objects.all()
    serializer_class = LeaveTransactionSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class PublicHolidayViewSet(viewsets.ModelViewSet):
    queryset = PublicHoliday.objects.all()
    serializer_class = PublicHolidaySerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class OnboardingViewSet(viewsets.ModelViewSet):
    queryset = Onboarding.objects.all()
    serializer_class = OnboardingSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class SalaryStructureViewSet(viewsets.ModelViewSet):
    queryset = SalaryStructure.objects.all()
    serializer_class = SalaryStructureSerializer

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

class LoanAdvanceViewSet(viewsets.ModelViewSet):
    queryset = LoanAdvance.objects.all()
    serializer_class = LoanAdvanceSerializer

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

class SkillDevelopmentViewSet(viewsets.ModelViewSet):
    queryset = SkillDevelopment.objects.all()
    serializer_class = SkillDevelopmentSerializer

class PerformanceKPIViewSet(viewsets.ModelViewSet):
    queryset = PerformanceKPI.objects.all()
    serializer_class = PerformanceKPISerializer

class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
