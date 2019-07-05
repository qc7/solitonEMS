from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # Pages
    path('', views.payroll_records_page, name="payroll_records_page"),
    path('edit_period_page/<int:id>/',views.edit_period_page,name="edit_period_page"),
    path('payroll_record_page',views.payroll_record_page,name="payroll_record_page"),
    # Processing
    path('add_period/', views.add_period, name="add_period"),
    path('delete_period/<int:id>/',views.delete_period,name="delete_period"),
    path('edit_period/',views.edit_period,name="edit_period")
]