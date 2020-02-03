from django.urls import path

from training import views

urlpatterns = [
    path('user_training_page', views.user_training_page, name="user_training_page")
]