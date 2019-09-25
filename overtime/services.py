from django.http import HttpResponseRedirect
from django.urls import reverse

from overtime.models import OvertimeApplication


def approve_overtime_application_finally(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.status = "Approved"
    overtime_application.save()
    return overtime_application


def reject_overtime_application_finally(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.status = "Rejected"
    overtime_application.save()
    return overtime_application


def hod_reject_overtime_application(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.HOD_approval = 'Rejected'
    overtime_application.save()
    return overtime_application


def cfo_reject_overtime_application(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.cfo_approval = 'Rejected'
    overtime_application.save()
    return overtime_application


def ceo_reject_overtime_application(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.ceo_approval = 'Rejected'
    overtime_application.save()
    return overtime_application


def hod_approve_overtime_application(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.HOD_approval = 'Approved'
    overtime_application.save()
    return overtime_application


def cfo_approve_overtime_application(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.cfo_approval = 'Approved'
    overtime_application.save()
    return overtime_application


def ceo_approve_overtime_application(id):
    # Get the overtime application
    overtime_application = OvertimeApplication.objects.get(pk=id)
    overtime_application.ceo_approval = 'Approved'
    overtime_application.save()
    return overtime_application


def amend_overtime_service(request):
    overtime_application_id = request.POST.get('id')
    overtime_application = OvertimeApplication.objects.get(pk=overtime_application_id)
    overtime_application.date = request.POST.get('date')
    overtime_application.start_time = request.POST.get('start_time')
    overtime_application.end_time = request.POST.get('end_time')
    overtime_application.description = request.POST.get('description')
    overtime_application.save()
    return overtime_application
