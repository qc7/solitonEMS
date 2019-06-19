from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Employee
# Create your views here.

# Authentication

# dashboard
@login_required
def dashboard_page(request):
    # # The line requires the user to be authenticated before accessing the view responses. 
    # if not request.user.is_authenticated:
    #     # if the user is not authenticated it renders a login page 
    #     return render(request,'registration/login.html',{"message":None})

    context = {
        "dashboard_page": "active"
    }
    return render(request,'employees/dashboard.html', context) 

@login_required
def employees_page(request):
    # The line requires the user to be authenticated before accessing the view responses. 
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page 
        return render(request,'registration/login.html',{"message":None})
    context = {
        "employees_page": "active",
        "employees": Employee.objects.all()

    }
    return render(request,'employees/employees.html', context)
    
@login_required
def leave_page(request):
    # The line requires the user to be authenticated before accessing the view responses. 
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page 
        return render(request,'registration/login.html',{"message":None})
    context = {
        "leave_page": "active"
    }
    return render(request,'employees/leave.html', context)


@login_required
def employee_page(request,id):
    # The line requires the user to be authenticated before accessing the view responses. 
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page 
        return render(request,'registration/login.html',{"message":None})
    
    employee = Employee.objects.get(pk=id)
    context = {
        "employees_page": "active",
        "employee": employee
    }
    return render(request,'employees/employee.html', context)

@login_required
def payroll_page(request):
    # The line requires the user to be authenticated before accessing the view responses. 
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page 
        return render(request,'registration/login.html',{"message":None})

    context = {
        "payroll_page": "active"
    }
    return render(request,'employees/payroll.html', context)

@login_required
def edit_employee_page(request,id):
    # The line requires the user to be authenticated before accessing the view responses. 
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page 
        return render(request,'registration/login.html',{"message":None})
    employee = Employee.objects.get(pk=id)
    context = {
        "employees_page": "active",
        "employee": employee
    }
    return render(request,'employees/edit_employee.html', context)

# The login view authenticates the user
# The view also renders the login page
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('dashboard_page'))
    
    else:
        return render(request, "registration/login.html", {"message":"Invalid credentials"})
        
def login_page(request):
    return render(request, "registration/login.html")

# The logout view logs out the user
def logout_view(request):
    logout(request)
    return render(request, "registration/login.html", {"message":"Logged Out","info":"info"})



# Process
@login_required
def add_new_employee(request):
    if request.method == 'POST':
        # Fetching data from the add new employee form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        position  = request.POST['position']
        gender = request.POST['gender']
        marital_status = request.POST['marital_status']
        start_date = request.POST['start_date']
        nationality = request.POST['nationality']
        nssf_no    = request.POST['nssf_no']
        ura_tin = request.POST['ura_tin']
        national_id = request.POST['national_id']
        telephone = request.POST['telephone']
        residence_address = request.POST['residence_address']
        dob = request.POST['dob']

        try:
            # Creating instance of Employee
            employee = Employee(first_name=first_name,last_name=last_name,position=position,gender=gender,
            marital_status= marital_status, start_date=start_date,nationality=nationality,nssf_no=nssf_no,
            ura_tin=ura_tin,national_id=national_id,telephone_no=telephone,residence_address=residence_address,
            dob=dob)
            # Saving the employee instance
            employee.save()
            context = {
                "employees_page": "active",
                "success_msg": "You have successfully added %s to the employees"%(employee.first_name)
            }

            return render(request,'employees/success.html',context)

        except:
            context ={
                "employees_page": "active",
                "failed_msg": "Failed! Something went wrong. Contact Bright and Hakim"
            }
            return render(request,"employees/failed.html",context)
 
    else :
        context ={
                "employees_page": "active",
                "failed_msg": "Failed! You performed a GET request"
            }
            
        return render(request,"employees/failed.html",context)
            
@login_required
def delete_employee(request,id):
    try:
    # Grab the employee
        employee = Employee.objects.get(pk=id)

        name = employee.first_name + " "+ employee.last_name
    # Delete the employee
        employee.delete()

    except Employee.DoesNotExist:
        context = {
        "employees_page": "active",
        "deleted_msg": "The employee no longer exists on the system"
        }

        return render(request, 'employees/deleted.html',context)

    context = {
        "employees_page": "active",
        "deleted_msg": "You have deleted %s from employees"%(name)
    } 
    return render(request, 'employees/deleted.html',context)