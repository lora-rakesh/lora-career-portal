from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ['referral_code']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'skills': forms.HiddenInput(),  # for JS-controlled skills field
        }
