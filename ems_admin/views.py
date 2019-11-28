from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from ems_admin.forms import UserForm, SolitonUserForm
from ems_admin.selectors import get_bound_user_form, get_user, get_solitonuser
from ems_auth.models import SolitonUser

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
            user.set_password('solitonug')
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


def edit_user_page(request, id):
    user = get_user(id)
    user_form = get_bound_user_form(user)

    try:
        solitonuser = get_solitonuser(user)
        soliton_user_form = get_bound_soliton_user_form(solitonuser)
    except SolitonUser.DoesNotExist:
        soliton_user_form = SolitonUserForm()

    if request.POST:
        soliton_user_form = SolitonUserForm(request.POST, instance=solitonuser)
        soliton_user_form.save(commit=False)
        user = UserForm(request.POST, instance=user)
        user.save()
        soliton_user_form.user = user
        soliton_user_form.save()

        return HttpResponseRedirect(reverse(manage_users_page))
    else:
        user = request.user
        context = {
            "user": user,
            "admin": "active",
            "user_form": user_form,
            "soliton_user_form": soliton_user_form

        }

        return render(request, 'ems_admin/edit_user.html', context)


def get_bound_soliton_user_form(solitonuser):
    soliton_user_form = SolitonUserForm(instance=solitonuser)
    return soliton_user_form


def view_users_page(request):
    user = request.user
    context = {
        "user": user,
        "admin": "active",
        "users": User.objects.all(),

    }
    return render(request, 'ems_admin/view_users.html', context)
