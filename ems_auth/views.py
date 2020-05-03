from django.contrib.auth import logout

from django.shortcuts import render

# Create your views here.
from ems_admin.activities import login_activity_response
from ems_admin.decorators import log_activity


def login_view(request):
    if request.POST:
        login_data = request.POST
        return login_activity_response(request, **login_data)
    else:
        return render(request, "ems_auth/login.html")


@log_activity
def login_page(request):
    return render(request, "ems_auth/login.html")


# The logout view logs out the user
@log_activity
def logout_view(request, activity_name="Logout user"):
    logout(request)
    return render(request, "ems_auth/login.html", {"message": "Logged Out", "info": "info"})


def super_admin_required_page(request):
    context = {
        "admin": "active",
    }

    return render(request, "ems_auth/super_admin_required.html", context)


@log_activity
def hr_required_page(request):
    return render(request, "ems_auth/hr_required.html", )


@log_activity
def hod_required_page(request):
    return render(request, "ems_auth/hod_required.html", )
