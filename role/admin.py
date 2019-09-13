from django.contrib import admin

from .models import SolitonUser,Notification
# Register your models here.
admin.site.register(SolitonUser)
admin.site.register(Notification)
