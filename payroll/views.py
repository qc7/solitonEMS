from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import PayrollRecord,Payroll
from django.urls import reverse
from .EmployeePayroll import EmployeePayroll
from employees.models import Employee
from django.db.models import Sum
# Create your views here.
# Pages
###############################################################
@login_required
def payroll_records_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})
    
    # Grab the payroll objects for this payroll record

    context = {
        "payroll_page": "active",
        "payroll_records": PayrollRecord.objects.all()
    }
    return render(request, 'payroll/payroll_records.html', context)

@login_required
def payroll_record_page(request,id):
    # Get the payroll record
    payroll_record = PayrollRecord.objects.get(pk=id)

    month = payroll_record.month
    year = payroll_record.year

    # Get all the associated Payroll objects
    payrolls = Payroll.objects.filter(payroll_record=payroll_record)
    context = {
        "payroll_page": "active",
        "month": month,
        "year": year,
        "payrolls": payrolls,
        "payroll_record": payroll_record
    }
    return render(request,'payroll/payroll_record.html',context) 

@login_required
def edit_period_page(request,id):
    # fetch PayrollRecordRequest 
    payroll_record = PayrollRecord.objects.get(pk=id)

    context = {
        "payroll_record": payroll_record,
        "payroll_page": "active"
    }

    return render(request,'payroll/edit_payroll.html',context)

@login_required
def payslip_page(request,id):
    # Get the payroll
    payroll = Payroll.objects.get(pk=id)

    context = {
        "payroll_page": "active",
        "payroll": payroll,
        "month": payroll.payroll_record.month,
        "year": payroll.payroll_record.year,
        "name_of_employee":"{} {}".format(payroll.employee.first_name,payroll.employee.last_name)
    }

    return render(request,'payroll/payslip.html',context)

###############################################################
# Processes
###############################################################

def add_period(request):
    # Fetch data from the add period form
    month = request.POST['month']
    year  = request.POST['year']
    # Create payroll instance
    payroll_record = PayrollRecord(month = month, year = year)
    # Save payroll
    payroll_record.save()

    return HttpResponseRedirect(reverse('payroll_records_page'))
    
def delete_period(request,id):
    # Grab the payroll record
    payroll_record = PayrollRecord.objects.get(pk=id)
    # Delete the payrool_record
    payroll_record.delete()
    return HttpResponseRedirect(reverse('payroll_records_page'))

def edit_period(request):
    # Fetch values
    payroll_record_id = request.POST['payroll_record_id']
    month = request.POST['month']
    year = request.POST['year']
    # Fetch the PayrollRecord
    payroll_record = PayrollRecord(pk=payroll_record_id)
    # Overwrite old values
    payroll_record.month = month
    payroll_record.year = year
    # Save payroll record
    payroll_record.save()

    return HttpResponseRedirect(reverse('payroll_records_page'))


def generate_payroll(request,id):
    # Get Payroll record
    payroll_record = PayrollRecord.objects.get(pk=id)
    # Get all employees
    employees = Employee.objects.all()
    # Loop through all employees
    for employee in employees:
       
        sacco_deduction = "0.0"
        damage_deduction ="0.0"
        total_deduction = 0
        if employee.deduction_set.filter(name="Sacco"):
            deduction = employee.deduction_set.filter(name="Sacco").first()
            sacco_deduction = str(deduction.amount)

        if employee.deduction_set.filter(name="Damage"):
            deduction = employee.deduction_set.filter(name="Damage").first()
            damage_deduction = str(deduction.amount)

        if employee.deduction_set.all():
            sum = employee.deduction_set.aggregate(Sum('amount'))
            total_deduction = sum['amount__sum']

        employee_payroll = EmployeePayroll(int(employee.basic_salary))
        employee_payroll.deduct(total_deduction)
        employee_nssf = employee_payroll.nssf_contrib
        employer_nssf = employee_payroll.employer_nssf_contrib
        gross_salary   = employee_payroll.gross_salary
        paye      = employee_payroll.paye
        net_salary = employee_payroll.net_salary
        total_nssf_contrib = int(employee_nssf) + int(employer_nssf)
        total_statutory = total_nssf_contrib + int(paye)
        

        # Create payroll object
        payroll = Payroll(employee=employee,payroll_record=payroll_record,employee_nssf=employee_nssf,
        employer_nssf=employer_nssf,gross_salary=gross_salary,paye=paye,net_salary=net_salary,
          total_nssf_contrib=total_nssf_contrib,total_statutory=total_statutory,
          sacco_deduction=sacco_deduction,damage_deduction=damage_deduction)

        # Save payroll object
        payroll.save()

    return HttpResponseRedirect(reverse('payroll_record_page', args=[payroll_record.id]))