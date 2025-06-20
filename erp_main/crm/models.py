from django.db import models
from django.conf import settings


class CompanyDetail(models.Model):
    organization_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    taxation_detail_id = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company detail"
        verbose_name_plural = "Company details"

    def __str__(self):
        return self.name


class IndividualContact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(CompanyDetail, related_name='contacts', on_delete=models.SET_NULL, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    taxation_detail_id = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Individual contact"
        verbose_name_plural = "Individual contacts"

    def __str__(self):
        return self.name


class Lead(models.Model):
    lead_id = models.AutoField(primary_key=True)
    contact = models.ForeignKey(IndividualContact, related_name='leads', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_leads', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        return f"{self.title} ({self.name})"


class Opportunity(models.Model):
    opportunity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    stage_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    lead = models.ForeignKey(Lead, related_name='opportunities', on_delete=models.SET_NULL, blank=True, null=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_opportunities', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Opportunity"
        verbose_name_plural = "Opportunities"

    def __str__(self):
        return self.name


class Proposal(models.Model):
    proposal_id = models.AutoField(primary_key=True)
    opportunity = models.ForeignKey(Opportunity, related_name='proposals', on_delete=models.CASCADE)
    contact = models.ForeignKey(IndividualContact, related_name='proposals', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_proposals', on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proposal"
        verbose_name_plural = "Proposals"

    def __str__(self):
        return self.name


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    lead = models.ForeignKey(Lead, related_name='activities', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    activity = models.ForeignKey(Activity, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title


class Meeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    activity = models.ForeignKey(Activity, related_name='meetings', on_delete=models.CASCADE)
    link = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timing = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"

    def __str__(self):
        return self.title




