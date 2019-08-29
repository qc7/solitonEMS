from django.urls import path
from role.views import employee_views

urlpatterns = [
    # Pages
    path('employee_leave_page/<int:id>/', employee_views.leave_page, name='employee_leave_page'),
    path('employee_payslip_page/<int:id>/', employee_views.employee_payslip_page, name="employee_payslip_page"),
    path('employee_overtime_page/<int:id>/', employee_views.employee_overtime_page, name="employee_overtime_page"),
    #     Process
    path('employee_overtime_application/',employee_views.apply_overtime,name="apply_overtime")
]
