from django.urls import path

from ems_admin.views import manage_users_page, view_users_page, edit_user_page

urlpatterns = [
    path('manage_users_page/', manage_users_page, name="manage_users_page"),
    path('edit_user_page/<int:id>/', edit_user_page, name="edit_user_page"),
    path('view_users_page/', view_users_page, name="view_users_page"),
]
