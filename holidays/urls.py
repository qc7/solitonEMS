from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pages
    path('', views.holidays_page, name="holidays_page"),
    path('delete_holiday/<int:holiday_id>/', views.delete_holiday, name="delete_holiday"),
    path('edit_holiday/<int:holiday_id>/', views.edit_holiday_page, name="edit_holiday_page"),
    
]