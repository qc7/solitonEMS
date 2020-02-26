from django.contrib.auth import get_user_model

from ems_admin.models import EMSPermission
from ems_admin.selectors import get_user
from ems_auth.services import save_audit_trail

User = get_user_model()





