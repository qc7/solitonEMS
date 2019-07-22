
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # Pages
    path('', views.dashboard_page, name="dashboard_page"),
    path('employees/', views.employees_page, name="employees_page"),
    path('employee/<int:id>/', views.employee_page, name="employee_page"),
    path('edit_employee_page/<int:id>/', views.edit_employee_page, name="edit_employee_page"),
    path('edit_certification_page/<int:id>/', views.edit_certification_page, name="edit_certification_page"),
    path('edit_emergency_contact_page/<int:id>/',views.edit_emergency_contact_page, name="edit_emergency_contact_page"),
    path('edit_beneficiary_page/<int:id>/',views.edit_beneficiary_page, name="edit_beneficiary_page"),
    path('edit_spouse_page/<int:id>/',views.edit_spouse_page, name="edit_spouse_page"),
    path('edit_dependant_page/<int:id>/',views.edit_dependant_page, name="edit_dependant_page"),
    path('departments/', views.departments_page, name="departments_page"),
    path('teams/<int:id>/', views.teams_page, name="teams_page"),
    path('jobs/', views.job_titles_page, name="job_titles_page"),

    # Process
    path('add_new_employee/', views.add_new_employee, name="add_new_employee"),
    path('delete_employee/<int:id>',views.delete_employee, name="delete_employee"),
    path('edit_employee/<int:id>',views.edit_employee, name="edit_employee"),
    path('add_new_home_address/', views.add_new_home_address, name="add_new_home_address"),
    path('edit_home_address/', views.edit_home_address, name="edit_home_address"),
    path('add_certification/', views.add_certification, name="add_certification"),
    path('delete_certification/<int:id>', views.delete_certification, name="delete_certification"),
    path('edit_certification/', views.edit_certification, name="edit_certification"),
    path('add_emergency_contact', views.add_emergency_contact, name="add_emergency_contact"),
    path('delete_emergency_contact/<int:id>', views.delete_emergency_contact, name="delete_emergency_contact"),
    path('edit_emergency_contact', views.edit_emergency_contact, name="edit_emergency_contact"),
    path('add_beneficiary/', views.add_beneficiary, name="add_beneficiary"),
    path('edit_beneficiary/', views.edit_beneficiary, name="edit_beneficiary"),
    path('delete_beneficiary/<int:id>/', views.delete_beneficiary, name="delete_beneficiary"),
    path('add_spouse/', views.add_spouse, name="add_spouse"),
    path('edit_spouse/', views.edit_spouse, name="edit_spouse"),
    path('delete_spouse/<int:id>', views.delete_spouse, name="delete_spouse"),
    path('add_dependant/', views.add_dependant, name="add_dependant"),
    path('edit_dependant/', views.edit_dependant, name="edit_dependant"),
    path('delete_dependant/<int:id>', views.delete_dependant, name="delete_dependant"),

     path('add_new_deparment/', views.add_new_department, name="add_new_department"),
     path('add_new_team/', views.add_new_team, name="add_new_team"),
     path('add_new_title/', views.add_new_title, name="add_new_title"),

    path('add_deduction/', views.add_deduction,name="add_deduction"),
    path('delete_deduction/<int:id>',views.delete_deduction,name="delete_deduction"),
    path('edit_bank_details/',views.edit_bank_details,name="edit_bank_details"),
    path('add_bank_details/',views.add_bank_details,name="add_bank_details"),
    # Authentication
    path('accounts/login/', views.login_page, name="loginAccounts"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]