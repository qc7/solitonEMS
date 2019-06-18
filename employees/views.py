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




