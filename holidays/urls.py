from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pages
    path('', views.holidays_page, name="holidays_page"),
    
]