from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def login_view(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard_page'))
        else:
            return render(request, "ems_auth/login.html", {"message": "Invalid Credentials"})
    else:
        return render(request, "ems_auth/login.html")


def login_page(request):
    return render(request, "ems_auth/login.html")


# The logout view logs out the user
def logout_view(request):
    logout(request)
    return render(request, "ems_auth/login.html", {"message": "Logged Out", "info": "info"})


def super_admin_required_page(request):
    context = {
        "admin": "active",
    }

    return render(request, "ems_auth/super_admin_required.html", context)


def hr_required_page(request):

    return render(request, "ems_auth/hr_required.html",)
