from django.contrib import admin

# Register your models here.
from .models import Employee,HomeAddress,Certification,EmergencyContact,Beneficiary,Spouse,Dependant,Deduction,BankDetail,Teams,Departments,Job_Titles

admin.site.register(Employee)
admin.site.register(HomeAddress)
admin.site.register(Certification)
admin.site.register(EmergencyContact)
admin.site.register(Beneficiary)
admin.site.register(Spouse)
admin.site.register(Dependant)
admin.site.register(Deduction)
admin.site.register(BankDetail)
admin.site.register(Teams)
admin.site.register(Departments)
admin.site.register(Job_Titles)