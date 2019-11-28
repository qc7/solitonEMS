from django.contrib.auth import get_user_model

from ems_admin.forms import UserForm
from ems_auth.models import SolitonUser

User = get_user_model()


def get_user(id) -> User:
    user = User.objects.get(pk=id)
    return user


def get_bound_user_form(user):
    return UserForm(instance=user)


def get_solitonuser(user):
    solitonuser = SolitonUser.objects.get(user=user)
    return solitonuser
