from django.contrib.auth import get_user_model

from ems_admin.forms import UserForm, SolitonUserForm, SolitonUserEditForm
from ems_admin.models import EMSPermission, AuditTrail
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
    soliton_user_form = SolitonUserEditForm(instance=solitonuser)
    return soliton_user_form


def create_soliton(user):
    pass


def get_solitonuser(user):
    try:
        solitonuser = SolitonUser.objects.get(user=user)
    except SolitonUser.DoesNotExist:
        return None
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
    permission = EMSPermission.objects.get(pk=id)
    return permission


def get_recent_audit_trails(user_id):
    user = get_user(user_id)
    audit_trails = AuditTrail.objects.filter(user=user).order_by('-id')
    return audit_trails


def get_all_recent_audit_trails():
    audit_trails = AuditTrail.objects.all().order_by('-id')
    return audit_trails
