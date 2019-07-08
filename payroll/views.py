from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import PayrollRecord
from django.urls import reverse

# Create your views here.
# Pages
###############################################################
@login_required
def payroll_records_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    context = {
        "payroll_page": "active",
        "payroll_records": PayrollRecord.objects.all()
    }
    return render(request, 'payroll/payroll_records.html', context)

@login_required
def payroll_record_page(request):
    context = {
        "payroll_page": "active"
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


    