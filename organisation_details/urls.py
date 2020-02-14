from django.urls import path

from . import views


urlpatterns = [
    path('', views.about_us, name="about_us"),
    path('no_organisation_detail_page/', views.no_organisation_detail_page, name="no_organisation_detail_page"),

    # departments
    path('edit_department_page/<int:id>/', views.edit_department_page, name="edit_department_page"),
    path('departments/', views.departments_page, name="departments_page"),
    path('add_new_deparment/', views.add_new_department, name="add_new_department"),
    path('edit_department/<int:id>', views.edit_department, name="edit_department"),
    path('delete_department/<int:id>', views.delete_department, name="delete_department"),

    # Teams
    path('add_new_team/', views.add_new_team, name="add_new_team"),
    path('teams/<int:id>/', views.teams_page, name="teams_page"),

    # Job Titles
    path('jobs/', views.job_titles_page, name="job_titles_page"),
    path('add_new_title/', views.add_new_title, name="add_new_title"),
    path('edit_job_title_page/<int:id>', views.edit_job_title_page, name="edit_job_title_page"),
    path('edit_job_title/<int:id>', views.edit_job_title, name="edit_job_title"),
    path('delete_job_title/<int:id>', views.delete_job_title, name="delete_job_title"),
]
