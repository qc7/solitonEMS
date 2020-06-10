from django.urls import path

from . import views


urlpatterns = [
    path('', views.about_us, name="about_us"),
    path('no_organisation_detail_page/', views.no_organisation_detail_page, name="no_organisation_detail_page"),

    # departments
    path('edit_department_page/<int:department_id>/', views.edit_department_page, name="edit_department_page"),
    path('manage_departments/', views.manage_departments_page, name="manage_departments_page"),
    path('add_new_department/', views.add_new_department, name="add_new_department"),
    path('edit_department', views.edit_department, name="edit_department"),
    path('delete_department/<int:department_id>', views.delete_department, name="delete_department"),

    # Teams
    path('add_new_team/', views.add_new_team, name="add_new_team"),
    # path('teams/<int:id>/', views.teams_page, name="teams_page"),
    path('edit_team_page/<int:id>/', views.edit_team_page, name="edit_team_page"),
    # path('edit_team/<int:id>/', views.edit_team, name="edit_team"),
    path('delete_team/<int:id>/', views.delete_team, name="delete_team"),
    path('teams', views.manage_teams_page, name="manage_teams_page"),
    path('edit_team/<team_id>/', views.edit_team_page, name="edit_team_page"),
    path('delete_team/<team_id>/', views.delete_team, name="delete_team"),

    # Job Positions
    path('manage_job_positions/', views.manage_job_positions_page, name="manage_job_positions_page"),
    path('add_new_job_position/', views.add_new_job_position, name="add_new_job_position"),
    path('edit_job_position/<int:position_id>', views.edit_job_position_page, name="edit_job_position_page"),
    path('edit_job_position/', views.edit_job_position, name="edit_job_position"),
    path('delete_job_position/<int:position_id>', views.delete_job_position, name="delete_job_position"),
]
