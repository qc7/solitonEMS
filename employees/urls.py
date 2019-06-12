
from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard_page, name="dashboard_page"),
    path('employees/', views.employees_page, name="employees_page"),
    path('payroll/', views.payroll_page, name="payroll_page"),
]