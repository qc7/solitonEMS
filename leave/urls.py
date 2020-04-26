from django.urls import path, reverse
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    # Pages 
    path('', views.leave_dashboard_page, name="leave_dashboard_page"),
    path('leave_records/', views.leave_records, name="leave_records"),
    path('add_leave_records/', views.add_leave_records, name="add_leave_records"),
    path('types/', views.leave_types_page, name="leave_types_page"),
    path('holidays/', views.holidays_page, name="holidays_page"),
    path('apply/', views.apply_leave_page, name="apply_leave_page"),
    
    # Process
    path('add_new_type/', views.add_new_type, name="add_new_type"),
    path('edit_type/<int:id>/', views.edit_leave_type_page, name="edit_leave_type_page"),
    path('add_new_holiday/', views.add_new_holiday, name="add_new_holiday"),
    path('apply_leave/', views.apply_leave, name="apply_leave"),
    path('approve_leave/', views.approve_leave, name="approve_leave"),
    path('reject_leave/', views.reject_leave, name="reject_leave"),
    path('get_end_date/', views.get_end_date, name="get_end_date"),  
    path('get_no_of_days/', views.get_no_of_days, name="get_no_of_days"),   
    
    path('annual_calendar/', views.Leave_planner_summary, name="annual_calendar"),
    path('leave_planner/', views.leave_planer, name="leave_planner"),
    path('add_new_absence/', views.add_new_absence, name="add_new_absence"),
    path('Leave_planner_summary/', views.Leave_planner_summary, name="Leave_planner_summary"),
    path('leave_calendar/', views.leave_calendar, name="Leave_calendar"),
    
]

def javascript_settings():
    js_conf = {
        'get_end_date': reverse('get_end_date'),
        'get_no_of_days': reverse('get_no_of_days'),
    }

    return js_conf