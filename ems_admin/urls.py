from django.urls import path

from ems_admin.views import manage_users_page, view_users_page, edit_user_page, manage_user_permissions_page, \
    edit_user_permission_page, user_audit_trail, audit_trails

urlpatterns = [
    path('manage_users_page/', manage_users_page, name="manage_users_page"),
    path('edit_user_page/<int:id>/', edit_user_page, name="edit_user_page"),
    path('manage_user_permissions_page/<int:id>/', manage_user_permissions_page, name="manage_user_permissions_page"),
    path('edit_user_permission_page/<int:id>/', edit_user_permission_page, name="edit_user_permission_page"),
    path('view_users_page/', view_users_page, name="view_users_page"),
    path('user_audit_trail/<int:user_id>/', user_audit_trail, name="user_audit_trail"),
    path('audit_trails/', audit_trails, name="audit_trails")

]
