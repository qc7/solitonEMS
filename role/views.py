from django.shortcuts import render
from employees.models import Employee
from payroll.models import PayrollRecord,Payroll
from leave.models import LeaveApplication,Leave_Types
# Create your views here.



def leave_page(request,id):
    # Get the employee
    employee = Employee.objects.get(pk=id)

    leave_applications = LeaveApplication.objects.all()
    context = {
        "apps": leave_applications,
        "l_types":Leave_Types.objects.all()
    }
    return render(request,'role/employee/leave.html',context)

def employee_payslip_page(request,id):
    # Get the employee
    employee = Employee.objects.get(pk=id)
    # Get the latest payroll record
    payroll_record = PayrollRecord.objects.all().order_by('-id')[0]

    # Get the payroll
    payroll = Payroll.objects.get(employee=employee,payroll_record=payroll_record)

    context = {
        "payroll": payroll,
        "month": payroll.payroll_record.month,
        "year": payroll.payroll_record.year,
        "name_of_employee":"{} {}".format(payroll.employee.first_name,payroll.employee.last_name)
    }
    return render(request,'role/employee/payslip.html',context)