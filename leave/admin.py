from django.contrib import admin

# Register your models here.
from .models import Leave_Types,LeaveApplication

admin.site.register(Leave_Types)
admin.site.register(LeaveApplication)