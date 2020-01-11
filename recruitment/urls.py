from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('manage_job_advertisement_page', views.manage_job_advertisement_page, name="manage_job_advertisement_page"),
]
