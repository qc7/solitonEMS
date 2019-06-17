
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.dashboard_page, name="dashboard_page"),
    path('employees/', views.employees_page, name="employees_page"),
    path('payroll/', views.payroll_page, name="payroll_page"),
    path('employee/', views.employee_page, name="employee_page"),
    path('accounts/login/', views.login_page, name="loginAccounts"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
] 