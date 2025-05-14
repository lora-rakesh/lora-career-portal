from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'education', 'experience', 'referral_code')
    search_fields = ('full_name', 'email', 'phone', 'referral_code', 'submitted_at')
    list_filter = ('education', 'experience', 'relocate')

admin.site.register(Applicant, ApplicantAdmin)