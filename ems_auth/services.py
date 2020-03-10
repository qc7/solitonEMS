from ems_admin.models import AuditTrail


def save_audit_trail(user, activity_name):
    audit_trail = AuditTrail.objects.create(
        user=user,
        activity_name=activity_name
    )

    return audit_trail
