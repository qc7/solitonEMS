from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
@login_required
def payroll_page(request):
    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    context = {
        "payroll_page": "active"
    }
    return render(request, 'payroll/payroll.html', context)