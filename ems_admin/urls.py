from django.urls import path

from ems_admin.views import manage_users_page, view_users_page, edit_user_page, manage_user_permissions_page, \
    edit_user_permission_page

urlpatterns = [
    path('manage_users_page/', manage_users_page, name="manage_users_page"),
    path('edit_user_page/<int:id>/', edit_user_page, name="edit_user_page"),
    path('manage_user_permissions_page/<int:id>/', manage_user_permissions_page, name="manage_user_permissions_page"),
    path('edit_user_permission_page/<int:id>/', edit_user_permission_page, name="edit_user_permission_page"),
    path('view_users_page/', view_users_page, name="view_users_page"),
]
