from django.contrib.auth import get_user_model

from ems_admin.selectors import get_user
from ems_auth.services import save_audit_trail

User = get_user_model()


def log_activity(function):
    def wrapper(request, **kw):
        try:
            user_id = request.user.id
            user = get_user(user_id)
            activity_name = function.__name__
            save_audit_trail(user, activity_name)
            return function(request, **kw)

        except User.DoesNotExist:
            return function(request, **kw)

    return wrapper


