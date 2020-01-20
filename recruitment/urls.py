from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('manage_job_advertisement_page', views.manage_job_advertisement_page, name="manage_job_advertisement_page"),
    path('edit_job_advertisement_page/<int:job_advertisement_id>/', views.edit_job_advertisement_page,
         name="edit_job_advertisement_page"),
    path('delete_job_advertisement/<int:job_advertisement_id>/', views.delete_job_advertisement,
         name="delete_job_advertisement"),
    path('job_advertisements_page', views.job_advertisements_page, name="job_advertisements_page"),
    path('view_job_applications_page', views.view_job_applications_page, name="view_job_applications_page"),
    path('job_advertisement/<int:job_advertisement_id>/', views.job_advertisement, name="job_advertisement"),
    path('job_applications/<int:job_advertisement_id>/', views.job_applications_page, name="job_applications"),
]
