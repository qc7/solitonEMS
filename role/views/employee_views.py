from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from employees.models import Employee
from overtime.models import OvertimeApplication
from payroll.models import PayrollRecord, Payroll
from leave.models import LeaveApplication, Leave_Types
from leave.procedures import get_leave_balance, get_employee_leave, leave_balance


# Create your views here.
from role.models import Notification


def leave_page(request, id):
    # Get the employee
    employee = Employee.objects.get(pk=id)

    leave_applications = LeaveApplication.objects.filter(employee=employee)
    context = {
        "leave_applications": leave_applications,
        "l_types": Leave_Types.objects.all(),
        "l_balance": employee.leave_balance,
    }
    return render(request, 'role/employee/leave.html', context)


def employee_payslip_page(request, id):
    # Get the employee
    employee = Employee.objects.get(pk=id)
    # Get the latest payroll record
    payroll_record = PayrollRecord.objects.all().order_by('-id')[0]

    # Get the payroll
    payroll = Payroll.objects.get(employee=employee, payroll_record=payroll_record)

    context = {
        "payroll": payroll,
        "month": payroll.payroll_record.month,
        "year": payroll.payroll_record.year,
        "name_of_employee": "{} {}".format(payroll.employee.first_name, payroll.employee.last_name)
    }
    return render(request, 'role/employee/payslip.html', context)


def employee_overtime_page(request, id):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    # Get the notifications
    user = request.user.solitonuser
    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()

    # Get the employee
    employee = Employee.objects.get(pk=id)
    # Get the pending overtime applications
    pending_applications = OvertimeApplication.objects.filter(status="Pending",applicant=employee)
    context = {
    "overtime_page": "active",
    "pending_applications": pending_applications
    }
    return render(request, 'role/employee/pending_overtime_applications.html', context)

def employe_approved_overtime_page(request, id):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    # Get the notifications
    user = request.user.solitonuser
    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()

    # Get the employee
    employee = Employee.objects.get(pk=id)
    # Get the approved overtime applications
    pending_applications = OvertimeApplication.objects.filter(status="Approved",applicant=employee)
    context = {
    "overtime_page": "active",
    "pending_applications": pending_applications
    }

    return render(request, 'role/employee/approved_overtime_applications.html', context)


@login_required
def apply_overtime(request):
    overtime_date = request.POST['date']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    description = request.POST['description']
    employee_id = request.POST['employee_id']
    applicant = Employee.objects.get(pk=employee_id)
    overtime_application = OvertimeApplication(date=overtime_date,start_time=start_time,end_time=end_time,description=description,applicant=applicant)
    overtime_application.save()
    return HttpResponseRedirect(reverse('employee_overtime_page',args=[employee_id]))