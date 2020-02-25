from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def ems_login_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if user.is_authenticated:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(reverse('login'))

    return wrapper


def super_admin_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if user.is_superuser:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(reverse('super_admin_required_page'))

    return wrapper


def hr_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if user.is_hr:
            return function(request, *args, **kw)
        else:
            return HttpResponseRedirect(reverse('hr_required_page'))

    return wrapper


def first_login(function):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if not user.password_changed:
            user.password_changed = True
            user.save()
            logout(request)
            return render(request, "ems_auth/first_time_login.html")
        else:
            return function(request, *args, **kwargs)

    return wrapper
