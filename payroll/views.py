import csv,io
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import PayrollRecord,Payroll
from django.urls import reverse
from .EmployeePayroll import EmployeePayroll
from employees.models import Employee
from django.db.models import Sum
from .procedures import get_total_deduction,get_total_nssf,get_total_paye,get_total_gross_pay,get_total_basic_pay,get_total_net_pay
from role.models import Notification,SolitonUser
# Create your views here.
# Pages
###############################################################
@login_required
def payroll_records_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})
    
    # Get the notifications
    user = request.user.solitonuser

    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()

    context = {
        "payroll_page": "active",
        "payroll_records": PayrollRecord.objects.all(),
        "number_of_notifications": number_of_notifications,
        "notifications":notifications
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
    # Get all employees
    employees = Employee.objects.all()

    # Get the notifications
    user = request.user.solitonuser

    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()

    context = {
        "payroll_page": "active",
        "month": month,
        "year": year,
        "payrolls": payrolls,
        "payroll_record": payroll_record,
        "total_nssf_contribution": get_total_nssf(payrolls),
        "total_paye": get_total_paye(payrolls),
        "total_gross_pay":get_total_gross_pay(payrolls),
        "total_basic_pay":get_total_basic_pay(employees),
        "total_net_pay":get_total_net_pay(payrolls),
        "number_of_notifications": number_of_notifications,
        "notifications":notifications
    }
    return render(request,'payroll/payroll_record.html',context) 

@login_required
def edit_period_page(request,id):
    # fetch PayrollRecordRequest 
    payroll_record = PayrollRecord.objects.get(pk=id)

    # Get the notifications
    user = request.user.solitonuser

    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()
    context = {
        "payroll_record": payroll_record,
        "payroll_page": "active",
        "number_of_notifications": number_of_notifications,
        "notifications":notifications
    }

    return render(request,'payroll/edit_payroll.html',context)

@login_required
def payslip_page(request,id):
    # Get the payroll
    payroll = Payroll.objects.get(pk=id)
    
    # Get the notifications
    user = request.user.solitonuser

    notifications = Notification.objects.filter(user=user)
    number_of_notifications = notifications.count()

    context = {
        "payroll_page": "active",
        "payroll": payroll,
        "month": payroll.payroll_record.month,
        "year": payroll.payroll_record.year,
        "name_of_employee":"{} {}".format(payroll.employee.first_name,payroll.employee.last_name),
        "number_of_notifications": number_of_notifications,
        "notifications":notifications
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
        
        if employee.deduction_set.filter(name="Sacco"):
            deduction = employee.deduction_set.filter(name="Sacco").first()
            sacco_deduction = str(deduction.amount)

        if employee.deduction_set.filter(name="Damage"):
            deduction = employee.deduction_set.filter(name="Damage").first()
            damage_deduction = str(deduction.amount)
   
        # Get total deduction
        total_deduction = get_total_deduction(employee)

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

def generate_payroll_with_bonus(request,id):
    # Get Payroll record
    payroll_record = PayrollRecord.objects.get(pk=id)
    # Get all employees
    employees = Employee.objects.all()
    # Loop through all employees
    for employee in employees:
        
        sacco_deduction = "0.0"
        damage_deduction ="0.0"
        
        if employee.deduction_set.filter(name="Sacco"):
            deduction = employee.deduction_set.filter(name="Sacco").first()
            sacco_deduction = str(deduction.amount)

        if employee.deduction_set.filter(name="Damage"):
            deduction = employee.deduction_set.filter(name="Damage").first()
            damage_deduction = str(deduction.amount)

        # Get total deduction
        total_deduction = get_total_deduction(employee)

        employee_payroll = EmployeePayroll(int(employee.basic_salary))
        
        bonus  = employee_payroll.get_half_bonus()

        employee_nssf = employee_payroll.get_nssf_contrib(employee_payroll.gross_salary)
        employer_nssf = employee_payroll.get_employer_nssf_contrib(employee_payroll.gross_salary)
        gross_salary   = employee_payroll.gross_salary
        paye      = employee_payroll.get_paye(employee_payroll.gross_salary)
        employee_payroll.get_net_salary(employee_payroll.gross_salary)
        employee_payroll.deduct(total_deduction)
        net_salary = employee_payroll.net_salary
        total_nssf_contrib = int(employee_nssf) + int(employer_nssf)
        total_statutory = total_nssf_contrib + int(paye)
        
        

        # Create payroll object
        payroll = Payroll(employee=employee,payroll_record=payroll_record,employee_nssf=employee_nssf,
        employer_nssf=employer_nssf,gross_salary=gross_salary,paye=paye,net_salary=net_salary,
            total_nssf_contrib=total_nssf_contrib,total_statutory=total_statutory,
            sacco_deduction=sacco_deduction,damage_deduction=damage_deduction,bonus=bonus)

        # Save payroll object
        payroll.save()

    return HttpResponseRedirect(reverse('payroll_record_page', args=[payroll_record.id]))


def add_prorate(request):
    # Fetch values from the form
    num_of_days_worked = request.POST['no_of_days_worked']
    payroll_id = request.POST['payroll_id']

    # Grab the Payroll object
    payroll = Payroll.objects.get(pk=payroll_id)

    # Grab the basic salary
    basic_salary = payroll.employee.basic_salary

    # Create the EmployeePayroll object
    employee_payroll = EmployeePayroll(basic_salary)

    # Check if the the payroll has bonus and overtime
    if payroll.bonus:
        employee_payroll.gross_salary = employee_payroll.gross_salary + int(payroll)

    if payroll.overtime:
        if payroll.overtime == '0.0':
            employee_payroll.add_overtime_amount(0)
        else:  
            employee_payroll.add_overtime_amount(payroll.overtime)

    # Add prorate to the employee payroll object
    employee_payroll.add_prorate(num_of_days_worked)

    # Subtract the deductions
    employee = payroll.employee

    total_deduction = get_total_deduction(employee)

    employee_payroll.deduct(total_deduction)

    # Update the payroll object 
    payroll.prorate = employee_payroll.prorate
    payroll.employee_nssf = int(employee_payroll.nssf_contrib)
    payroll.employer_nssf = int(employee_payroll.employer_nssf_contrib)
    payroll.gross_salary   = int(employee_payroll.gross_salary)
    payroll.paye      = int(employee_payroll.paye)
    payroll.net_salary = int(employee_payroll.net_salary)
    payroll.total_nssf_contrib = int(payroll.employee_nssf) + int(payroll.employer_nssf)
    payroll.total_statutory = payroll.total_nssf_contrib + int(payroll.paye)
    
    # Save the payroll object
    payroll.save()

    return HttpResponseRedirect(reverse('payslip_page', args=[payroll.id]))

def add_bonus(request):
    # Fetch values from the form
    bonus = request.POST['bonus']
    payroll_id = request.POST['payroll_id']

    # Grab the Payroll object
    payroll = Payroll.objects.get(pk=payroll_id)

    # Grab the basic salary
    basic_salary = payroll.employee.basic_salary

    # Create the EmployeePayroll object
    employee_payroll = EmployeePayroll(basic_salary)

    # Check if the overtime is set
    if payroll.overtime:
        employee_payroll.add_overtime_amount(float(payroll.overtime))

    # Add bonus to the employee payroll object
    employee_payroll.add_bonus(bonus)

    # Subtract the deductions
    employee = payroll.employee

    total_deduction = get_total_deduction(employee)

    employee_payroll.deduct(total_deduction)

    # Update the payroll object
    payroll.bonus = employee_payroll.bonus
    payroll.employee_nssf = int(employee_payroll.nssf_contrib)
    payroll.employer_nssf = int(employee_payroll.employer_nssf_contrib)
    payroll.gross_salary   = int(employee_payroll.gross_salary)
    payroll.paye      = int(employee_payroll.paye)
    payroll.net_salary = int(employee_payroll.net_salary)
    payroll.total_nssf_contrib = int(payroll.employee_nssf) + int(payroll.employer_nssf)
    payroll.total_statutory = payroll.total_nssf_contrib + int(payroll.paye)
    
    # Save the payroll object 
    payroll.save()

    return HttpResponseRedirect(reverse('payslip_page', args=[payroll.id]))

def add_overtime(request):

    # Fetch values from the form
    number_of_hours_normal = request.POST['number_of_hours_normal']
    number_of_hours_holidays = request.POST['number_of_hours_holidays']
    payroll_id = request.POST['payroll_id']

    # Grab the Payroll object
    payroll = Payroll.objects.get(pk=payroll_id)

    # If the payroll already has bonus
    if float(payroll.bonus) > 0:
        context = {
            "payroll_page": "active",
            "payroll": payroll
        }
        return render(request,'payroll/failed.html',context)

    # Grab the basic salary
    basic_salary = payroll.employee.basic_salary

    # Create the EmployeePayroll object
    employee_payroll = EmployeePayroll(basic_salary)

    # Add overtime to the employee payroll object
    total_overtime = 0
    if number_of_hours_normal:
        overtime = employee_payroll.add_overtime(int(number_of_hours_normal),False)
        total_overtime = total_overtime + overtime
        
    if number_of_hours_holidays:
        overtime = employee_payroll.add_overtime(int(number_of_hours_holidays),True)
        total_overtime = total_overtime + overtime
    
    # Subtract the deductions
    employee = payroll.employee

    total_deduction = get_total_deduction(employee)

    # Update the payroll object
    payroll.gross_salary   = int(employee_payroll.gross_salary)
    payroll.overtime = int(total_overtime)
    payroll.employee_nssf = int(employee_payroll.get_nssf_contrib(payroll.gross_salary))
    payroll.employer_nssf = int(employee_payroll.get_employer_nssf_contrib(payroll.gross_salary))
    payroll.paye      = int(employee_payroll.get_paye(payroll.gross_salary))
    employee_payroll.get_net_salary(payroll.gross_salary)
    employee_payroll.deduct(total_deduction)
    payroll.net_salary = int(employee_payroll.net_salary)
    payroll.total_nssf_contrib = int(payroll.employee_nssf) + int(payroll.employer_nssf)
    payroll.total_statutory = payroll.total_nssf_contrib + int(payroll.paye)
    
    # Save the payroll object
    payroll.save()

    return HttpResponseRedirect(reverse('payslip_page', args=[payroll.id]))


@login_required
def payroll_download(request,id):
    # Get the payroll record
    payroll_record = PayrollRecord.objects.get(pk=id)
    month = payroll_record.month
    year = payroll_record.year
    # Get all the associated Payroll objects
    payrolls = Payroll.objects.filter(payroll_record=payroll_record)
    response = HttpResponse(content_type='text/csv')
    # Name the csv file
    filename = "payroll_"+month+"_"+year+".csv"
    response['Content-Disposition'] = 'attachment; filename='+filename
    writer = csv.writer(response,delimiter=',')
    # Writing the first row of the csv
    heading_text = "Payroll for "+ month + " "+ year
    writer.writerow([heading_text.upper()])
    writer.writerow(['Name','Employee NSSF Contribution','Employer NSSF contribution','PAYE','Bonus','Sacco Deduction','Damage Deduction','Basic Salary','Lunch Allowance','Overtime','Gross Salary','Net Salary'])
    # Writing other rows
    for payroll in payrolls:
        name = payroll.employee.first_name + " " + payroll.employee.last_name
        writer.writerow([name,payroll.employee_nssf,payroll.employer_nssf,payroll.paye,payroll.bonus,payroll.sacco_deduction,payroll.damage_deduction,payroll.employee.basic_salary,150000,payroll.overtime,payroll.gross_salary,payroll.net_salary,])

    # Return the response
    return response




