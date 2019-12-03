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
        return render(request, 'ems_auth/login.html', {"message": "Wrong or No role assigned."})