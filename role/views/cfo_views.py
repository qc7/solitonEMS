from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from employees.models import Employee
from overtime.models import OvertimeApplication
from payroll.models import PayrollRecord, Payroll
from leave.models import LeaveApplication, Leave_Types
from leave.procedures import get_leave_balance, get_employee_leave, leave_balance


def cfo_role_page(request):
    context = {
        "dashboard_page": "active",
    }
    return render(request, "role/cfo/dashboard.html", context)


def cfo_overtime_page(request):
    # Get the pending overtime applications
    pending_applications = OvertimeApplication.objects.filter(status="Pending")
    context = {
        "overtime_page": "active",
        "pending_applications": pending_applications
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