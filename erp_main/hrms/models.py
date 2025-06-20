from django.db import models
from django.db import models
from user_auth.models import Organization



class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='departments'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.name


class Designation(models.Model):
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=100)
    hierarchy_level = models.IntegerField()
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='designations'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'designations'

    def __str__(self):
        return f"{self.title} (Level {self.hierarchy_level})"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    employment_type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, default='active')
    hired_date = models.DateField(blank=True, null=True)

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='employees'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True, blank=True
    )
    designation = models.ForeignKey(
        Designation,
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True, blank=True
    )
    reports_to = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='subordinates',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendances'
    )
    date = models.DateTimeField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    work_hours = models.FloatField(default=0)
    overtime = models.FloatField(default=0)
    break_time = models.FloatField(default=0)
    location = models.TextField(blank=True, null=True)
    is_remote = models.BooleanField(default=False)
    punch_method = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'attendance'


class Bonus(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='bonuses'
    )
    amount = models.FloatField()
    bonus_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    approved_by = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_bonuses'
    )
    approval_date = models.DateTimeField(null=True, blank=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bonus'

    def __str__(self):
        return f"Bonus #{self.id} - {self.status}"


class ComplianceRecord(models.Model):
    record_id = models.CharField(primary_key=True, max_length=100)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='compliance_records'
    )
    compliance_status = models.CharField(max_length=50)
    recorded_at = models.DateTimeField()

    class Meta:
        db_table = 'compliance_records'

    def __str__(self):
        return f"{self.record_id} - {self.compliance_status}"


class EmployeeBenefit(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='benefits'
    )
    health_plan = models.CharField(max_length=255, blank=True, null=True)
    retirement_plan = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee_benefits'


class EmployeeDocument(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='documents'
    )
    document_name = models.CharField(max_length=255)
    document_url = models.TextField()
    expiry_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee_documents'


class EmployeeExit(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='exits'
    )
    exit_type = models.CharField(max_length=100)
    exit_date = models.DateTimeField()
    clearance_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee_exits'

    def __str__(self):
        return f"Exit #{self.id} - {self.exit_type} ({self.clearance_status})"


class EmployeePerk(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='perks'
    )
    perk = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee_perks'


class Expense(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='expenses'
    )
    expense_type = models.CharField(max_length=255)
    amount = models.FloatField()
    status = models.CharField(max_length=50, default='pending')
    date = models.DateTimeField(auto_now_add=True)
    approver = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_expenses'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'expenses'

    def __str__(self):
        return f"Expense #{self.id} - {self.expense_type} - {self.status}"


class Feedback(models.Model):
    feedback_id = models.CharField(max_length=100, primary_key=True)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    feedback_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback'


class Grievance(models.Model):
    grievance_id = models.CharField(primary_key=True, max_length=100)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='grievances'
    )
    issue = models.TextField()
    status = models.CharField(max_length=50, default='Filed')
    filed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grievances'

    def __str__(self):
        return f"Grievance #{self.grievance_id} - {self.status}"


class AnalyticsReport(models.Model):
    report_name = models.CharField(max_length=255)
    report_data = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'analytics_reports'

    def __str__(self):
        return f"{self.report_name} ({self.generated_at.strftime('%Y-%m-%d')})"

from django.db import models

class LeaveType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LeavePolicy(models.Model):
    organization_id = models.BigIntegerField()
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    max_days = models.IntegerField()
    carry_forward = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('organization_id', 'leave_type')

    def __str__(self):
        return f"{self.leave_type.name} policy for Org {self.organization_id}"

class LeaveBalance(models.Model):
    employee_id = models.BigIntegerField()
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    total_leaves = models.IntegerField()
    used_leaves = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('employee_id', 'leave_type')

    @property
    def remaining_leaves(self):
        return self.total_leaves - self.used_leaves

class LeaveTransaction(models.Model):
    class ActionChoices(models.TextChoices):
        DEDUCT = 'DEDUCT', 'Deduct'
        RESTORE = 'RESTORE', 'Restore'
        ADJUST = 'ADJUST', 'Adjust'

    employee_id = models.BigIntegerField()
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    change_amount = models.IntegerField()
    action = models.CharField(max_length=10, choices=ActionChoices.choices)
    reason = models.TextField(blank=True, null=True)
    performed_by = models.BigIntegerField(blank=True, null=True)
    performed_at = models.DateTimeField(auto_now_add=True)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PublicHoliday(models.Model):
    organization_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} on {self.date}"

class Job(models.Model):
    job_id = models.CharField(max_length=64, primary_key=True)
    title = models.CharField(max_length=255)
    department_id = models.CharField(max_length=64)
    description = models.TextField()
    requirements = models.TextField()
    employment_type = models.CharField(max_length=50)
    salary_range_start = models.FloatField()
    salary_range_end = models.FloatField()
    location = models.CharField(max_length=255)
    posted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.job_id})"

class Applicant(models.Model):
    applicant_id = models.CharField(max_length=64, primary_key=True)
    job = models.ForeignKey(Job, related_name="applicants", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume_url = models.URLField()
    status = models.CharField(max_length=50)
    applied_at = models.DateTimeField()

    def __str__(self):
        return f"{self.full_name} - {self.status}"

class Interview(models.Model):
    interview_id = models.CharField(max_length=64, primary_key=True)
    applicant = models.ForeignKey(Applicant, related_name="interviews", on_delete=models.CASCADE)
    interviewer = models.CharField(max_length=255)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Interview {self.interview_id} for {self.applicant.full_name}"

class Onboarding(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        IN_PROGRESS = 'In Progress', 'In Progress'
        COMPLETED = 'Completed', 'Completed'

    onboarding_id = models.CharField(max_length=64, primary_key=True)
    employee_id = models.CharField(max_length=64)
    department_id = models.CharField(max_length=64)
    assigned_manager = models.CharField(max_length=64, blank=True, null=True)
    required_documents = models.JSONField(default=list)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Onboarding({self.employee_id} - {self.status})"

class Shift(models.Model):
    SHIFT_TYPE_CHOICES = [
        ('DAY', 'Day'),
        ('NIGHT', 'Night'),
        ('FLEXIBLE', 'Flexible'),
    ]

    name = models.CharField(max_length=100)
    shift_type = models.CharField(max_length=20, choices=SHIFT_TYPE_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = models.JSONField()

    def __str__(self):
        return f"{self.name} ({self.shift_type})"

class SalaryStructure(models.Model):
    organization_id = models.BigIntegerField()
    designation_id = models.BigIntegerField()
    base_salary = models.FloatField()
    allowances = models.FloatField()
    tax_percentage = models.FloatField()
    deductions = models.FloatField()

    def __str__(self):
        return f"SalaryStructure (Org: {self.organization_id}, Designation: {self.designation_id})"

class Payroll(models.Model):
    employee_id = models.BigIntegerField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    tax = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    allowances = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    deductions = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, default="Pending")
    payslip_url = models.TextField(blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_number = models.CharField(max_length=64, blank=True, null=True)
    branch_code = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payroll #{self.id} for Employee {self.employee_id}"

class LoanAdvance(models.Model):
    class LoanStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'

    employee_id = models.BigIntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    purpose = models.TextField()
    status = models.CharField(max_length=10, choices=LoanStatus.choices, default=LoanStatus.PENDING)
    approved_by = models.BigIntegerField(blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    repayment_start = models.DateTimeField(blank=True, null=True)
    repayment_months = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



class PerformanceReview(models.Model):
    employee_id = models.BigIntegerField()
    reviewer_id = models.BigIntegerField()
    review_date = models.DateTimeField()
    review_period = models.CharField(max_length=100)
    overall_rating = models.IntegerField()
    feedback = models.TextField()
    promotion = models.BooleanField(default=False)



class SkillDevelopment(models.Model):
    review = models.ForeignKey(PerformanceReview, related_name="skills", on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    development_plan = models.TextField()

class PerformanceKPI(models.Model):
    review = models.ForeignKey(PerformanceReview, related_name="kpis", on_delete=models.CASCADE)
    kpi_name = models.CharField(max_length=255)
    score = models.FloatField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.kpi_name} - Score: {self.score}"

class WorkHistory(models.Model):
    employee_id = models.BigIntegerField()
    company = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    reason_for_exit = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company} - {self.designation}"
