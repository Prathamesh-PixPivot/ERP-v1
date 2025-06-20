from rest_framework import serializers
from .models import (
    Department, Designation, Employee, Attendance, Bonus, ComplianceRecord,
    EmployeeBenefit, EmployeeDocument, EmployeeExit, EmployeePerk, Expense,
    Feedback, Grievance, AnalyticsReport
)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = '__all__'

class ComplianceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceRecord
        fields = '__all__'

class EmployeeBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBenefit
        fields = '__all__'

class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocument
        fields = '__all__'

class EmployeeExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeExit
        fields = '__all__'

class EmployeePerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePerk
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class GrievanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grievance
        fields = '__all__'

class AnalyticsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsReport
        fields = '__all__'

from .models import (
    LeaveType, LeavePolicy, LeaveBalance, LeaveTransaction,
    Organization, PublicHoliday, Job, Applicant, Interview,
    Onboarding, Shift, SalaryStructure, Payroll, LoanAdvance,
    PerformanceReview, SkillDevelopment, PerformanceKPI, WorkHistory
)

class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = '__all__'

class LeavePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeavePolicy
        fields = '__all__'

class LeaveBalanceSerializer(serializers.ModelSerializer):
    remaining_leaves = serializers.IntegerField(read_only=True)

    class Meta:
        model = LeaveBalance
        fields = '__all__' + 'remaining_leaves'

class LeaveTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveTransaction
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class PublicHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicHoliday
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'

class OnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onboarding
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class SalaryStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryStructure
        fields = '__all__'

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'

class LoanAdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAdvance
        fields = '__all__'

class SkillDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillDevelopment
        fields = '__all__'

class PerformanceKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceKPI
        fields = '__all__'

class PerformanceReviewSerializer(serializers.ModelSerializer):
    skills = SkillDevelopmentSerializer(many=True, read_only=True)
    kpis = PerformanceKPISerializer(many=True, read_only=True)

    class Meta:
        model = PerformanceReview
        fields = '__all__' + 'skills' + 'kpis'

class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'
