from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # Pages
    path('', views.payroll_records_page, name="payroll_records_page"),
    path('edit_period_page/<int:id>/',views.edit_period_page,name="edit_period_page"),
    path('payroll_record_page/<int:id>/',views.payroll_record_page,name="payroll_record_page"),
    path('payslip_page/<int:id>',views.payslip_page,name='payslip_page'),
    # Processing
    path('add_period/', views.add_period, name="add_period"),
    path('delete_period/<int:id>/',views.delete_period,name="delete_period"),
    path('edit_period/',views.edit_period,name="edit_period"),
    path('generate_payroll/<int:id>', views.generate_payroll, name="generate_payroll"),
    path('generate_payroll_with_bonus/<int:id>', views.generate_payroll_with_bonus, name="generate_payroll_with_bonus"),
    path('add_prorate/',views.add_prorate, name="add_prorate"),
    path('add_bonus/',views.add_bonus,name="add_bonus"),
    path('add_overtime/',views.add_overtime,name="add_overtime"),
]