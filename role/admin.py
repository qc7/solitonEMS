from django.contrib import admin

from .models import SolitonRole,SolitonUser,Notification
# Register your models here.
admin.site.register(SolitonRole)
admin.site.register(SolitonUser)
admin.site.register(Notification)
