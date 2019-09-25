from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from employees.models import Employee,Supervision
from overtime.models import OvertimeApplication
from payroll.models import PayrollRecord, Payroll
from leave.models import LeaveApplication, Leave_Types
from leave.procedures import get_leave_balance, get_employee_leave, leave_balance
# Create your views here.
from role.models import Notification


def employee_role_page(request):
    user = request.user
    # If employee
    context = {
        "employee": user.solitonuser.employee,
        "view_profile_page": 'active'
    }
    return render(request, "role/employee/employee.html", context)

def leave_page(request, id):
    # Get the employee
    employee = Employee.objects.get(pk=id)

    leave_applications = LeaveApplication.objects.filter(employee=employee)
    context = {
        "leave_applications": leave_applications,
        "l_types": Leave_Types.objects.all(),
        "l_balance": employee.leave_balance,
        "leave_page": "active"
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
        "name_of_employee": "{} {}".format(payroll.employee.first_name, payroll.employee.last_name),
        "payslip_page": "active"
    }
    return render(request, 'role/employee/payslip.html', context)

def employee_overtime_page(request, id):

    # Get the employee
    employee = Employee.objects.get(pk=id)
    # Get the pending overtime applications
    pending_applications = OvertimeApplication.objects.filter(status="Pending",supervisee=employee)
    context = {
    "pending_applications": pending_applications,
    "overtime_page": "active"
    }
    return render(request, 'role/employee/pending_overtime_applications.html', context)

def employee_approved_overtime_page(request, id):
    # Get the employee
    employee = Employee.objects.get(pk=id)
    # Get the approved overtime applications
    approved_applications = OvertimeApplication.objects.filter(status="Approved",supervisee=employee)
    context = {
    "overtime_page": "active",
    "approved_applications": approved_applications
    }
    return render(request, 'role/employee/approved_overtime_applications.html', context)

def employee_rejected_overtime_page(request, id):
    # Get the employee
    employee = Employee.objects.get(pk=id)
    # Get the approved overtime applications
    approved_applications = OvertimeApplication.objects.filter(status="Rejected",supervisee=employee)
    context = {
    "overtime_page": "active",
    "approved_applications": approved_applications
    }
    return render(request, 'role/employee/rejected_overtime_page.html', context)

def employee_supervisees_page(request,id):
    # Get the employee
    employee = Employee.objects.get(pk=id)
    context = {
    "supervisees_page": "active",
    "supervisions": Supervision.objects.filter(supervisor=employee)
   
    }
    return render(request,'role/employee/supervisees.html',context)

def employee_supervisee_page(request,id):
    # Get the supervisee
    supervisee = Employee.objects.get(pk=id)
    # Get the supervisee
    supervisee = Employee.objects.get(pk=id)
    # Get the approved overtime applications
    pending_applications = OvertimeApplication.objects.filter(status="Pending",supervisee=supervisee)
    context = {
        "supervisees_page":"active",
        "supervisee": supervisee,
        "pending_applications": pending_applications
    }
    return render(request,'role/employee/supervisee.html',context)

@login_required
def apply_overtime(request):
    overtime_application = create_overtime_application(request)
    supervisee_id = overtime_application.supervisee.id
    return HttpResponseRedirect(reverse('employee_supervisee_page',args=[supervisee_id]))


def create_overtime_application(request):
    overtime_date = request.POST['date']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    description = request.POST['description']
    supervisee_id = request.POST['supervisee_id']
    supervisor_id = request.POST['supervisor_id']
    supervisor = Employee.objects.get(pk=supervisor_id)
    supervisee = Employee.objects.get(pk=supervisee_id)
    overtime_application = OvertimeApplication(date=overtime_date, start_time=start_time, end_time=end_time,
                                               supervisor=supervisor,
                                               description=description, supervisee=supervisee)
    overtime_application.save()
    return overtime_application