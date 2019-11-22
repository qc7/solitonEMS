from django.contrib import admin

# Register your models here.
from ems_auth.models import User

admin.site.register(User)
