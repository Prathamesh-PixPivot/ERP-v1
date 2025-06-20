from django.contrib import admin
from .models import (
    Opportunity,
    Proposal,
    Meeting,
    CompanyDetail,
    IndividualContact,
    Task,
    Activity,
    Lead,
)

admin.site.register(CompanyDetail)
admin.site.register(IndividualContact)
admin.site.register(Lead)
admin.site.register(Activity)
admin.site.register(Task)
admin.site.register(Opportunity)
admin.site.register(Proposal)
admin.site.register(Meeting)

