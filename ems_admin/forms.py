from django.db.models import TextField
from django.forms import ModelForm, EmailField, forms, CharField, TextInput, Field

from ems_auth.models import User, SolitonUser


class UserForm(ModelForm):
    email = EmailField(
        label='',
        required=True,
        widget=TextInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['email', 'is_superuser', 'is_staff', 'is_hr', 'is_hod', 'is_cfo', 'is_ceo']


class SolitonUserForm(ModelForm):
    class Meta:
        model = SolitonUser
        fields = ['employee']
