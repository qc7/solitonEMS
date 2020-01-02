from django.forms import ModelForm, DateField, CharField, Textarea, DateInput, \
    DateTimeField, DateTimeInput
from overtime.models import OvertimeApplication


class OvertimeApplicationForm(ModelForm):
    date = DateField(
        label='Date',
        required=True,
        widget=DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    start_time = DateTimeField(
        label='Start Time',
        required=True,
        widget=DateTimeInput(attrs={'class': 'form-control'})
    )

    end_time = DateTimeField(
        label='End Time',
        required=True,
        widget=DateTimeInput(attrs={'class': 'form-control'})
    )

    description = CharField(
        label='Description',
        required=True,
        widget=Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = OvertimeApplication
        fields = ['start_time', 'end_time', 'description']
