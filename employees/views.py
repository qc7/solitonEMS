from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
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
        "dashboard": "active"
    }
    return render(request,'employees/dashboard.html', context) 


def employees_page(request):
    # The line requires the user to be authenticated before accessing the view responses. 
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page 
        return render(request,'registration/login.html',{"message":None})
    context = {
        "employees": "active"
    }
    return render(request,'employees/employees.html', context)

def leave_page(request):
    # The line requires the user to be authenticated before accessing the view responses. 
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page 
        return render(request,'registration/login.html',{"message":None})
    context = {
        "leave": "active"
    }
    return render(request,'employees/leave.html', context)


def payroll_page(request):
    # The line requires the user to be authenticated before accessing the view responses. 
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page 
        return render(request,'registration/login.html',{"message":None})

    context = {
        "payroll": "active"
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


