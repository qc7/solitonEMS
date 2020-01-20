from django.forms import ModelForm

from recruitment.models import JobApplication


class JobApplicationForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cv']
