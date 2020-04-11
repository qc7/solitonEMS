from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('approve_overtime_page', views.approve_overtime_page, name="approve_overtime_page"),
    path('overtime_applications', views.overtime_applications_page, name="overtime_applications_page"),
    path('apply_for_overtime', views.apply_for_overtime_page, name="apply_for_overtime_page"),
    path('approved_overtime_applications/', views.approved_overtime_applications_page, name="approved_overtime_page"),
    path('amend_overtime_application/<int:overtime_application_id>', views.amend_overtime_application_page,
         name="amend_overtime_application_page"),
    path('pending_overtime_application/<int:overtime_application_id>', views.pending_overtime_application_page,
         name="pending_overtime_application_page"),
    path('create_overtime_plan_page/', views.create_overtime_plan_page, name="create_overtime_plan_page"),
    path('approve_overtime_plans_page/', views.approve_overtime_plans_page, name="approve_overtime_plans_page"),
    
    # Process
    path('reject_overtime/<int:overtime_application_id>', views.reject_overtime_application,
         name="reject_overtime_application"),
    path('approve_overtime/<int:overtime_application_id>', views.approve_overtime_application,
         name="approve_overtime_application"),

]
