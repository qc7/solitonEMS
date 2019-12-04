from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pages
    path('', views.overtime_page, name="overtime_page"),
    path('approved_overtime_applications/', views.approved_overtime_page, name="approved_overtime_page"),
    # Process
    path('reject_overtime/<int:id>', views.reject_overtime_application, name="reject_overtime_application"),
    path('approve_overtime/<int:id>', views.approve_overtime_application, name="approve_overtime_application"),

]
