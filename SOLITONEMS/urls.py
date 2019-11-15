
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('ems_auth/', include('ems_auth.urls')),
    path('admin/', admin.site.urls),
    path('payroll/',include('payroll.urls')),
    path('leave/',include('leave.urls')),
    path('role/',include('role.urls')),
    path('settings/',include('settings.urls')),
    path('overtime/',include('overtime.urls')),
    path('holidays/',include('holidays.urls')),
    path('',include('employees.urls')),

]
