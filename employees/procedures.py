from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from role.models import Notification
def redirect_user_role(request):
    user = request.user
    # If user is an employee
    if str(user.solitonuser.soliton_role) == 'Employee':
        return render(request,"role/employee.html")
    # If user is HOD
    if str(user.solitonuser.soliton_role) == 'HOD':
        return render(request,"role/ceo.html")

# Send notification
def send_notification(solitonuser,message):
    notification = Notification(user=solitonuser,message=message)
    notification.save()


def check_role(request, role, user):
    if role == 'HR' and user.solitonuser.is_hr == 'True':
        return HttpResponseRedirect(reverse('dashboard_page'))
    elif role == 'Employee':
        return HttpResponseRedirect(reverse('employee_role_page'))
    elif role == "HOD" and user.solitonuser.is_hod == 'True':
        return HttpResponseRedirect(reverse('hod_role_page'))
    elif role == "CFO" and user.solitonuser.is_cfo == 'True':
        return HttpResponseRedirect(reverse('cfo_role_page'))
    elif role == "CEO" and user.solitonuser.is_ceo == 'True':
        return HttpResponseRedirect(reverse('ceo_role_page'))
    else:
        return render(request, 'registration/login.html', {"message": "Wrong or No role assigned."})

