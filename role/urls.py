from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pages
    path('leave_page/<int:id>/',views.leave_page,name='leave_page'),
    path('employee_payslip_page/<int:id>/',views.employee_payslip_page,name="employee_payslip_page")
]