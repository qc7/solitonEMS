from django.contrib import admin

# Register your models here.
from contracts.models import Contract

admin.site.register(Contract)
