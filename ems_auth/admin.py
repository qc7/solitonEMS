from django.contrib import admin

# Register your models here.
from ems_auth.models import User, SolitonUser

admin.site.register(User)
admin.site.register(SolitonUser)
