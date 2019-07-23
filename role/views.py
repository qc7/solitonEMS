from django.shortcuts import render

# Create your views here.

def employee_home_page(request):
    # Grab employee
    user = request.user

    employee = user.solitonuser.employee

    context = {
        "employee": user.solitonuser.soliton_role
    }

    return render(request,'role/employees.html',context)

