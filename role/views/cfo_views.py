from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from overtime.models import OvertimeApplication
from overtime.selectors import get_cfo_pending_overtime_applications, get_overtime_application
from overtime.services import cfo_reject_overtime_application, cfo_approve_overtime_application, amend_overtime_service


def cfo_role_page(request):
    context = {
        "dashboard_page": "active",
    }
    return render(request, "role/cfo/dashboard.html", context)


def cfo_overtime_page(request):
    context = {
        "overtime_page": "active",
        "pending_applications": get_cfo_pending_overtime_applications()
    }
    return render(request, "role/cfo/overtime.html", context)


def cfo_overtime_approved_page(request):
    # Get the approved overtime applications
    approved_applications = OvertimeApplication.objects.filter(status="Approved")
    context = {
        "overtime_page": "active",
        "approved_applications": approved_applications
    }
    return render(request, "role/cfo/approved_applications_page.html", context)


def cfo_amend_overtime_page(request, id):
    overtime_application = get_overtime_application(id)
    context = {
        "overtime_page": "active",
        "overtime_application": overtime_application
    }
    return render(request,"role/cfo/amend_overtime.html",context)


# Process
def cfo_reject_overtime(request, id):
    cfo_reject_overtime_application(id)
    messages.success(request, "The overtime application was rejected")
    return HttpResponseRedirect(reverse('cfo_overtime_page'))


def cfo_approve_overtime(request, id):
    cfo_approve_overtime_application(id)
    messages.success(request, "The overtime application was approved")
    return HttpResponseRedirect(reverse('cfo_overtime_page'))


def cfo_amend_overtime(request):
    if request.method == 'POST':
        amend_overtime_service(request)
    return HttpResponseRedirect(reverse('cfo_overtime_page'))
