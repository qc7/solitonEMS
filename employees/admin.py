from django.contrib import admin

# Register your models here.
from .models import Employee,HomeAddress

admin.site.register(Employee)
admin.site.register(HomeAddress)