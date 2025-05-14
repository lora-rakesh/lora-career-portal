from django.db import models
from django.utils import timezone

class Applicant(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    education = models.CharField(max_length=50)
    graduation_year = models.IntegerField()
    skills = models.CharField(max_length=255)
    experience = models.FloatField()
    resume = models.FileField(upload_to='resumes/')
    job_role = models.CharField(max_length=100)
    current_company = models.CharField(max_length=100, blank=True, null=True)
    expected_salary = models.IntegerField(blank=True, null=True)
    notice_period = models.IntegerField(blank=True, null=True)
    relocate = models.CharField(max_length=10)
    referral_code = models.CharField(max_length=10, unique=True)
    submitted_at = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.full_name


