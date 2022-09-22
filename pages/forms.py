from django import forms

from .models import *

class JobDetailForm(forms.ModelForm):
	
    class Meta:
        model = Application
        fields = [
            'applicant_name',
            'applicant_phone',
            'applicant_email',
            'resume'
        ]