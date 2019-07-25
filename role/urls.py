from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pages
    path('employee_leave_page/<int:id>/',views.leave_page,name='employee_leave_page'),
    path('employee_payslip_page/<int:id>/',views.employee_payslip_page,name="employee_payslip_page")
]