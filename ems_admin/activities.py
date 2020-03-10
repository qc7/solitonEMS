from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_activity_response(request, **kwargs):
    data_dict = kwargs
    email = data_dict['email'][0]  # Get first array element
    password = data_dict['password'][0]  # Get first array element
    user = authenticate(username=email, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('dashboard_page'))
    else:
        return render(request, "ems_auth/login.html", {"message": "Invalid Credentials"})
