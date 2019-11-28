from django.contrib.auth import get_user_model

from ems_admin.forms import UserForm, SolitonUserForm
from ems_admin.models import EMSPermission
from ems_admin.services import create_default_permissions
from ems_auth.models import SolitonUser

User = get_user_model()


def get_user(id) -> User:
    user = User.objects.get(pk=id)
    return user


def get_bound_user_form(user):
    return UserForm(instance=user)


def get_bound_soliton_user_form(user):
    solitonuser = get_solitonuser(user)
    soliton_user_form = SolitonUserForm(instance=solitonuser)
    return soliton_user_form


def get_solitonuser(user):
    solitonuser = SolitonUser.objects.get(user=user)
    return solitonuser


def fetch_all_permissions(user):
    permissions = EMSPermission.objects.filter(user=user)
    return permissions


def fetch_all_permissions_or_create(user):
    permissions = fetch_all_permissions(user)

    if permissions:
        return permissions
    else:
        create_default_permissions(user)


def get_permission(id):
    permission = EMSPermission.objects.get(pk=1)
    return permission
