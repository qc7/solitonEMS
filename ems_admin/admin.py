from django.contrib import admin

# Register your models here.
from ems_admin.models import EMSPermission, AuditTrail

admin.site.register(EMSPermission)
admin.site.register(AuditTrail)