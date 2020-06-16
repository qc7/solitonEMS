from django.urls import path, reverse
from . import views

urlpatterns = [
    path('<int:id>/', views.notifications_page, name="notifications_page"),
]
