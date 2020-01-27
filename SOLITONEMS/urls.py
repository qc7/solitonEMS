from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('ems_auth/', include('ems_auth.urls')),
    path('admin/', admin.site.urls),
    path('payroll/', include('payroll.urls')),
    path('recruitment/', include('recruitment.urls')),
    path('leave/', include('leave.urls')),
    path('settings/', include('settings.urls')),
    path('overtime/', include('overtime.urls')),
    path('holidays/', include('holidays.urls')),
    path('', include('employees.urls')),
    path('ems_admin/', include('ems_admin.urls')),
    path('organisationdetails', include('organisation_details.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
