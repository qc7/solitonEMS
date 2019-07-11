from django.contrib import admin
from .models import Payroll, PayrollRecord
# Register your models here.

admin.site.register(PayrollRecord)
admin.site.register(Payroll)