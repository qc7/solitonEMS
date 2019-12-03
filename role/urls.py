from django.urls import path
from role.views import employee_views, hod_views, cfo_views, ceo_views

urlpatterns = [
    # Employee Pages
    path('employee_role_page', employee_views.employee_role_page, name="employee_role_page"),
    path('employee_leave_page/<int:id>/', employee_views.leave_page, name='employee_leave_page'),
    path('employee_payslip_page/<int:id>/', employee_views.employee_payslip_page, name="employee_payslip_page"),
    path('employee_approved_overtime_applications/<int:id>/', employee_views.employee_approved_overtime_page,
         name="employee_approved_overtime_page"),
    path('employee_rejected_overtime_applications/<int:id>/', employee_views.employee_rejected_overtime_page,
         name="employee_rejected_overtime_page"),
    path('employee_overtime_page/<int:id>/', employee_views.employee_overtime_page, name="employee_overtime_page"),
    path('employee_supervisees_page/<int:id>/', employee_views.employee_supervisees_page,
         name="employee_supervisees_page"),
    path('employee_supervisee_page/<int:id>/', employee_views.employee_supervisee_page,
         name="employee_supervisee_page"),
    #    Employee  Process
    path('employee_overtime_application/', employee_views.apply_overtime, name="apply_overtime"),

    # HOD Pages
    path('hod_role_page', hod_views.hod_role_page, name="hod_role_page"),
    path('hod_overtime_page', hod_views.hod_overtime_page, name="hod_overtime_page"),
    path('hod_amend_overtime_page/<int:id>/', hod_views.hod_amend_overtime_page, name="hod_amend_overtime_page"),
    # HOD Process
    path('hod_reject_overtime/<int:id>/', hod_views.hod_reject_overtime, name="hod_reject_overtime"),
    path('hod_approves_overtime/<int:id>/', hod_views.hod_approve_overtime, name="hod_approve_overtime"),
    path('hod_amend_overtime', hod_views.hod_amend_overtime, name="hod_amend_overtime"),
    # CFO Pages
    path('cfo_role_page', cfo_views.cfo_role_page, name="cfo_role_page"),
    path('cfo_overtime_page', cfo_views.cfo_overtime_page, name="cfo_overtime_page"),
    path('cfo_overtime_approved_page', cfo_views.cfo_overtime_approved_page, name="cfo_overtime_approved_page"),
    # Process
    path('cfo_reject_overtime/<int:id>/', cfo_views.cfo_reject_overtime, name="cfo_reject_overtime"),
    path('cfo_approve_overtime/<int:id>/', cfo_views.cfo_approve_overtime, name="cfo_approve_overtime"),
    path('cfo_amend_overtime/', cfo_views.cfo_amend_overtime, name="cfo_amend_overtime"),
    path('cfo_amend_overtime_page/<int:id>', cfo_views.cfo_amend_overtime_page, name="cfo_amend_overtime_page"),
    # CEO Pages
    path('ceo_role_page', ceo_views.ceo_role_page, name="ceo_role_page"),
    path('ceo_overtime_page', ceo_views.ceo_overtime_page, name="ceo_overtime_page"),
    path('ceo_overtime_approved_page', ceo_views.ceo_overtime_approved_page, name="ceo_overtime_approved_page"),
    path('ceo_amend_overtime_page/<int:id>/', ceo_views.ceo_amend_overtime_page,name="ceo_amend_overtime_page"),
    # CEO processes
    path('ceo_reject_overtime/<int:id>/', ceo_views.ceo_reject_overtime, name="ceo_reject_overtime"),
    path('ceo_approve_overtime/<int:id>/',ceo_views.ceo_approve_overtime, name="ceo_approve_overtime"),
]
