from django.urls import path

from ems_admin.views import manage_users_page, view_users_page

urlpatterns = [
    path('manage_users_page/', manage_users_page, name="manage_users_page"),
    path('view_users_page/', view_users_page, name="view_users_page"),
]
