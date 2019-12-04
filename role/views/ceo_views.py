from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from overtime.models import OvertimeApplication
from overtime.selectors import get_overtime_application, get_ceo_pending_overtime_applications
from overtime.services import ceo_reject_overtime_application, ceo_approve_overtime_application, \
    approve_overtime_application_finally


def ceo_role_page(request):
    context = {
        "dashboard_page": "active",
    }
    return render(request, "role/ceo/dashboard.html", context)


def ceo_overtime_page(request):
    # Get the pending overtime applications
    pending_applications = get_ceo_pending_overtime_applications()
    context = {
        "overtime_page": "active",
        "pending_applications": pending_applications
    }
    return render(request, "role/ceo/overtime.html", context)


def ceo_overtime_approved_page(request):
    # Get the approved overtime applications
    approved_applications = OvertimeApplication.objects.filter(status="Approved")
    context = {
        "overtime_page": "active",
        "approved_applications": approved_applications
    }
    return render(request, "role/ceo/approved_applications_page.html", context)


def ceo_amend_overtime_page(request, id):
    overtime_application = get_overtime_application(id)
    context = {
        "overtime_page": "active",
        "overtime_application": overtime_application
    }
    return render(request, "role/ceo/amend_overtime.html", context)


# Process
def ceo_reject_overtime(request, id):
    ceo_reject_overtime_application(id)
    messages.success(request, "The overtime application was rejected")
    context = {
        "overtime_page": "active"
    }
    return HttpResponseRedirect(reverse(ceo_overtime_page))


def ceo_approve_overtime(request, id):
    ceo_approve_overtime_application(id)
    approve_overtime_application_finally(id)
    messages.success(request, "The overtime application was approved")
    context = {
        "overtime": "active"
    }
    return HttpResponseRedirect(reverse(ceo_overtime_page))
