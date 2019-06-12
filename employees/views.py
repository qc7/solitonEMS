from django.shortcuts import render

# Create your views here.

# dashboard
def dashboard_page(request):
    context = {
        "dashboard": "active"
    }
    return render(request,'employees/dashboard.html', context) 

def employees_page(request):
    context = {
        "employees": "active"
    }
    return render(request,'employees/employees.html', context)

def payroll_page(request):
    context = {
        "payroll": "active"
    }
    return render(request,'employees/payroll.html', context)