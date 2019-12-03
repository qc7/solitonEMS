from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from overtime.models import OvertimeApplication
from overtime.selectors import get_hod_pending_overtime_applications
from overtime.services import hod_reject_overtime_application, hod_approve_overtime_application, \
    amend_overtime_service
from django.contrib import messages


def hod_role_page(request):
    context = {
        "dashboard_page": "active",
    }
    return render(request, "role/hod/dashboard.html", context)


def hod_overtime_page(request):
    user = request.user
    try:
        hod_pending_applications = get_hod_pending_overtime_applications(user)
    except:
        pending_applications = []
        context = {
            "overtime_page": "active",
            "pending_applications": pending_applications
        }
        return render(request, "role/hod/overtime.html", context)
    context = {
        "overtime_page": "active",
        "pending_applications": hod_pending_applications
    }
    return render(request, "role/hod/overtime.html", context)


def hod_amend_overtime_page(request, id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    context = {
        "overtime_page": "active",
        "overtime_application": overtime_application
    }
    return render(request, "role/hod/amend_overtime.html", context)


# Processes
def hod_reject_overtime(request, id):
    hod_reject_overtime_application(id)
    messages.success(request, "The overtime application was rejected")
    return HttpResponseRedirect(reverse('hod_overtime_page'))


def hod_approve_overtime(request, id):
    hod_approve_overtime_application(id)
    messages.success(request, "The overtime application was successfully approved")
    return HttpResponseRedirect(reverse('hod_overtime_page'))


def hod_amend_overtime(request):
    if request.method == 'POST':
        amend_overtime_service(request)
    messages.success(request, "Updated the overtime application")
    return HttpResponseRedirect(reverse('hod_overtime_page'))
