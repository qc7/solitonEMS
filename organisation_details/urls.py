from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.about_us, name="about_us"),
    path('no_organisation_detail_page/', views.no_organisation_detail_page, name="no_organisation_detail_page")
]
