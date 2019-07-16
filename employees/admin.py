from django.contrib import admin

# Register your models here.
from .models import Employee,HomeAddress,Certification,EmergencyContact,Beneficiary,Spouse,Dependant,Deduction

admin.site.register(Employee)
admin.site.register(HomeAddress)
admin.site.register(Certification)
admin.site.register(EmergencyContact)
admin.site.register(Beneficiary)
admin.site.register(Spouse)
admin.site.register(Dependant)
admin.site.register(Deduction)