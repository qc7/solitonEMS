from ems_admin.models import EMSPermission


def create_default_permissions(user):
    EMSPermission.objects.create(
        user=user,
        name="Manage Employees",
    )

    permissions = EMSPermission.objects.filter(user=user)
    return permissions
