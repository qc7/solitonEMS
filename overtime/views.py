from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from overtime.models import OvertimeApplication
from role.models import Notification


# Create your views here.
@login_required
def overtime_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    # Get the notifications
    user = request.user.solitonuser
    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()
    # Get the pending overtime applications
    pending_applications = OvertimeApplication.objects.filter(status="Pending")

    context = {
        "overtime_page": "active",
        "number_of_notifications": number_of_notifications,
        "notifications": notifications,
        "pending_applications": pending_applications
    }
    return render(request, 'overtime/overtime_page.html', context)

@login_required
def approved_overtime_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    # Get the notifications
    user = request.user.solitonuser
    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()
    # Get the approved overtime applications
    approved_applications = OvertimeApplication.objects.filter(status="Approved")

    context = {
        "overtime_page": "active",
        "number_of_notifications": number_of_notifications,
        "notifications": notifications,
        "approved_applications": approved_applications
    }
    return render(request, 'overtime/approved_applications_page.html', context)

def reject_overtime_application(request, id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)

    overtime_application.status = "Rejected"

    overtime_application.save()

    return HttpResponseRedirect(reverse('overtime_page'))


def approve_overtime_application(request, id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.status = "Approved"
    overtime_application.save()
    return HttpResponseRedirect(reverse('overtime_page'))


