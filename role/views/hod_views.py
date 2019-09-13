from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from employees.models import Employee
from overtime.models import OvertimeApplication
from payroll.models import PayrollRecord, Payroll
from leave.models import LeaveApplication, Leave_Types
from leave.procedures import get_leave_balance, get_employee_leave, leave_balance

def hod_role_page(request):
    context = {
        "dashboard_page": "active",
    }
    return render(request, "role/hod/dashboard.html",context)

def hod_overtime_page(request):
    # Get the pending overtime applications
    pending_applications = OvertimeApplication.objects.filter(status="Pending")
    context = {
        "overtime_page": "active",
        "pending_applications": pending_applications
    }
    return render(request, "role/hod/overtime.html", context)