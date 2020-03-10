from ems_admin.models import EMSPermission


def create_default_permissions(user):
    EMSPermission.objects.create(
        user=user,
        name="Employees",

    )

    EMSPermission.objects.create(
        user=user,
        name="Organisation",
    )

    EMSPermission.objects.create(
        user=user,
        name="Leave",
    )

    EMSPermission.objects.create(
        user=user,
        name="Payroll",
    )

    EMSPermission.objects.create(
        user=user,
        name="Overtime",
    )

    EMSPermission.objects.create(
        user=user,
        name="Holidays",
    )
    EMSPermission.objects.create(
        user=user,
        name="Recruitment",
    )

    EMSPermission.objects.create(
        user=user,
        name="Contracts",
    )

    EMSPermission.objects.create(
        user=user,
        name="Training",
    )

    EMSPermission.objects.create(
        user=user,
        name="Learning and Development",
    )

    EMSPermission.objects.create(
        user=user,
        name="Leave",
    )

    permissions = EMSPermission.objects.filter(user=user)
    return permissions
