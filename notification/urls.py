from django.urls import path, reverse
from . import views

urlpatterns = [
    path('notifications_page/', views.notifications_page, name="notifications_page"),
]
