from django.contrib import admin
from .models import Payslip, PayrollRecord
# Register your models here.

admin.site.register(PayrollRecord)
admin.site.register(Payslip)