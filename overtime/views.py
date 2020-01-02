from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ems_auth.decorators import ems_login_required
from overtime.forms import OvertimeApplicationForm
from overtime.models import OvertimeApplication
from overtime.selectors import get_all_overtime_applications, get_pending_overtime_applications, \
    get_overtime_application, get_recent_overtime_applications
from overtime.services import reject_overtime_application_service, approve_overtime_application_service


# Create your views here.
@ems_login_required
def approve_overtime_page(request):
    approver = request.user
    pending_applications = get_pending_overtime_applications(approver)
    context = {
        "overtime_page": "active",
        "pending_applications": pending_applications
    }
    return render(request, 'overtime/overtime_page.html', context)


@ems_login_required
def apply_for_overtime_page(request):
    if request.POST:
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        description = request.POST.get('description')

        applicant = request.user.solitonuser.employee

        overtime_application = OvertimeApplication.objects.create(
            start_time=start_time,
            end_time=end_time,
            description=description,
            applicant=applicant
        )
        messages.success(request, "You have successfully submitted your overtime application")

        return HttpResponseRedirect(reverse('apply_for_overtime_page'))

    recent_applications = get_recent_overtime_applications(limit=5)
    context = {
        "overtime_page": "active",
        "recent_applications": recent_applications
    }
    return render(request, 'overtime/overtime_application.html', context)


@ems_login_required
def overtime_applications_page(request):
    context = {
        "overtime_page": "active",
        "overtime_applications": get_all_overtime_applications()
    }

    return render(request, 'overtime/overtime_applications.html', context)


@ems_login_required
def approved_overtime_applications_page(request):
    # Get the approved overtime applications
    approved_applications = OvertimeApplication.objects.filter(status="Approved")
    context = {
        "overtime_page": "active",
        "approved_applications": approved_applications
    }
    return render(request, 'overtime/approved_applications_page.html', context)


def amend_overtime_application_page(request, overtime_application_id):
    overtime_application = get_overtime_application(overtime_application_id)
    if request.POST:
        OvertimeApplication.objects.filter(pk=overtime_application.id).update(
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time'),
            description=request.POST.get('description')
        )
        messages.success(request, "Successfully amended the overtime application")
        return HttpResponseRedirect(reverse('approve_overtime_page'))

    context = {
        "overtime_page": "active",
        "overtime_application": overtime_application
    }

    return render(request, 'overtime/amend_overtime_application.html', context)


def reject_overtime_application(request, overtime_application_id):
    rejecter = request.user
    overtime_application = get_overtime_application(overtime_application_id)
    rejected_overtime_application = reject_overtime_application_service(rejecter, overtime_application)
    if rejected_overtime_application:
        messages.success(request, "You rejected %s's overtime application" % rejected_overtime_application.applicant)
    else:
        messages.error(request, "You are not associated to any role on the system")
    return HttpResponseRedirect(reverse('approve_overtime_page'))


def approve_overtime_application(request, overtime_application_id):
    approver = request.user
    overtime_application = get_overtime_application(overtime_application_id)
    approved_overtime_application = approve_overtime_application_service(approver, overtime_application)
    if approved_overtime_application:
        messages.success(request, "You approved %s's overtime application" % approved_overtime_application.applicant)
    else:
        messages.error(request, "You are not associated to any role on the system")
    return HttpResponseRedirect(reverse('approve_overtime_page'))
