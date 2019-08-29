from django.shortcuts import render
from employees.models import Employee
from payroll.models import PayrollRecord,Payroll
from leave.models import LeaveApplication,Leave_Types
from leave.procedures import get_leave_balance, get_employee_leave, leave_balance
# Create your views here.


def get_current_user(request, need):
    user = request.user #getting the current logged in User

    cur_user = f'{user.solitonuser.employee.first_name} {user.solitonuser.employee.last_name}'
    cur_role = user.solitonuser.soliton_role.name
    user_dept = user.solitonuser.employee.organisationdetail.department.id
    cur_id = user.solitonuser.employee.id
    gender = user.solitonuser.employee.gender

    if need == "name":
        return cur_user
    elif need == "role":
        return cur_role
    elif need == "dept":
        return user_dept
    elif need == "id":
        return cur_id
    elif need == "gender":
        return gender
    else:
        return 0

def leave_page(request,id):
    # Get the employee
    employee = Employee.objects.get(pk=id)

    leave_applications = LeaveApplication.objects.filter(employee=employee)
    context = {  
        "leave_page": "active",
        "leave_applications": leave_applications,
        "l_types":Leave_Types.objects.all(),
        "l_balance": employee.leave_balance,    
        "gender": get_current_user(request, "gender")      
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