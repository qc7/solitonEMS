# Authentication
from django.urls import path
from ems_auth import views

urlpatterns = [
    path('accounts/login/', views.login_page, name="loginAccounts"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
