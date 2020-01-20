from django.contrib import admin

# Register your models here.
from recruitment.models import JobAdvertisement, JobApplication

admin.site.register(JobAdvertisement)
admin.site.register(JobApplication)
