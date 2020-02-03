from django.urls import path

from learning_and_development import views

urlpatterns = [
    path('manage_resources_page', views.manage_resources_page, name="manage_resources_page"),
    path('edit_resource_page/<int:resource_id>/', views.edit_resource_page, name="edit_resource_page"),
    path('delete_resource/<int:resource_id>/', views.delete_resource, name="delete_resource"),
    path('resources_page', views.resources_page, name="resources_page"),
    path('books_page', views.books_page, name="books_page"),
    path('videos_page', views.videos_page, name="videos_page"),
    path('audios_page', views.audios_page, name="audios_page"),

]
