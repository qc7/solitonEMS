from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from ems_admin.forms import UserForm, SolitonUserForm

User = get_user_model()


def manage_users_page(request):
    user = request.user
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user_form = UserForm(request.POST)
        soliton_user_form = SolitonUserForm(request.POST)
        # check whether it's valid:
        if user_form.is_valid() and soliton_user_form.is_valid():
            user = user_form.save(commit=False)
            user.password = "solitonug"
            user.save()
            soliton_user = soliton_user_form.save(commit=False)
            soliton_user.user = user
            soliton_user.save()

            return HttpResponseRedirect(reverse(manage_users_page))
        else:

            return HttpResponseRedirect(reverse(manage_users_page))
        # if a GET (or any other method) we'll create a blank form
    else:

        user_form = UserForm()
        soliton_user_form = SolitonUserForm()

        context = {
            "user": user,
            "admin": "active",
            "users": User.objects.all(),
            "user_form": user_form,
            "soliton_user_form": soliton_user_form

        }

        return render(request, 'ems_admin/manage_users.html', context)


def view_users_page(request):
    user = request.user
    context = {
        "user": user,
        "admin": "active",
        "users": User.objects.all(),

    }
    return render(request, 'ems_admin/view_users.html', context)
