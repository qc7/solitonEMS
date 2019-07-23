from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pages
    path('employee_home_page/',views.employee_home_page, name='employee_home_page')
]