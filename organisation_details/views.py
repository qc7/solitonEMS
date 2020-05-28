from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from employees.models import Employee
from employees.selectors import get_active_employees, get_employee
from ems_admin.decorators import log_activity
from ems_auth.decorators import hr_required, ems_login_required, organisation_full_auth_required
from organisation_details.models import Position, Department, Team
from organisation_details.selectors import (
    get_all_departments, 
    get_department, 
    get_position, 
    get_all_positions,
    get_all_teams,
    get_team
    )
from settings.selectors import get_all_currencies, get_currency


@log_activity
def about_us(request):
    return render(request, "organisation_description.html")


@log_activity
def no_organisation_detail_page(request):
    context = {
        "organisation_detail_page": "active"
    }
    return render(request, 'no_organisation_detail.html', context)


@hr_required
@organisation_full_auth_required
@log_activity
def departments_page(request):
    context = {
        "user": request.user,
        "organisation_page": "active",
        "departs": get_all_departments(),
        "emps": get_active_employees(),
    }

    return render(request, "employees/departments.html", context)


@hr_required
@log_activity
def teams_page(request, id):
    teams = Team.objects.filter(department=id)
    context = {
        "user": request.user,
        "employees_page": "active",
        "teams": teams,
        "dep": get_department(id),
        "emps": get_active_employees(),
    }
    return render(request, "employees/teams.html", context)


@ems_login_required
@hr_required
@organisation_full_auth_required
@log_activity
def job_titles_page(request):
    context = {
        "user": request.user,
        "organisation_page": "active",
        "positions": get_all_positions(),
        "currencies": get_all_currencies()
    }

    return render(request, "employees/job_titles.html", context)


# Department Section
@log_activity
def add_new_department(request):
    if request.method == "POST":
        print(request.POST["hod"])
        dep_name = request.POST["dep_name"]
        hod = get_employee(request.POST["hod"])

    try:
        depat = Department(name=dep_name, hod=hod)
        depat.save()
        messages.success(request, f'Info Successfully Saved')
        return redirect('departments_page')

    except:
        messages.error(request, f'Infor Not Saved, Check you inputs and try again!')

        return redirect('departments_page')


def edit_department(request, id):
    try:
        if request.method == "POST":
            department = get_department(id)

            name=request.POST.get('name')
            hod=get_employee(request.POST.get('hod'))
            status=request.POST.get('status')

            Department.objects.filter(id=department.id).update(
                name=name,
                hod=hod,
                status=status
            )
            # department.save()
            messages.success(request, f'Department Updated Successfully')
            return redirect('departments_page')

        else:
            messages.error(request, f'Update NOT Successfull')
            
            return redirect('departments_page')

    except:
        messages.error(request, f'Info Not Saved, Check you inputs and try again!')

    return redirect('departments_page')


@log_activity
def edit_department_page(request, id):
    context = {
        "user": request.user,
        "employee": get_active_employees(),
        "deps": get_department(id),
    }
    return render(request, 'employees/edit_department.html', context)

@log_activity
def edit_team_page(request, id):
    context = {
        "user": request.user,
        "employee": get_active_employees(),
        "teams": get_team(id),
    }
    return render(request, 'employees/edit_team.html', context)

@log_activity
def edit_team(request, id):
    if request.method == "POST":
        team=get_team(id)

        name = request.POST.get('name')
        supervisor = get_employee(request.POST.get('supervisor'))
        status = request.POST.get('status')
        department = request.POST.get('depart')

        Team.objects.filter(id=team.id).update(
            name=name,
            supervisors=supervisor,
            status=status
        )
        
        messages.success(request, f'Team Updated Successfully')
        return redirect(reverse('teams_page', kwargs={"id": department}))

    else:
        messages.error(request, f'Operation was NOT Successfull')
    
    
        return redirect('teams_page')


@log_activity
def delete_team(request, id):
    try:
        team = get_team(id)
        team.delete()
        messages.success(request, f'Team Deleted Successfully')
        
        return redirect(reverse('teams_page', kwargs={"id": team.department.id}))
    except Team.DoesNotExist:
        messages.error(request, f'The department no longer exists on the system')

        return redirect(reverse('teams_page', kwargs={"id": team.department.id}))

@log_activity
def delete_department(request, id):
    try:
        department = get_department(id)
        department.delete()
        messages.success(request, f'Department Deleted Successfully')
        return redirect('departments_page')
    except Department.DoesNotExist:
        messages.error(request, f'The department no longer exists on the system')

    return redirect('departments_page')


@log_activity
def add_new_team(request):
    if request.method == "POST":
        team_name = request.POST["team_name"]
        sup = request.POST["sups"]
        dpt = request.POST["dept"]

        try:
            supervisor = Employee.objects.get(pk=sup)
            team = Team(department_id=dpt, name=team_name, supervisors=supervisor)
            team.save()
            messages.success(request, f'Info Successfully Saved')

        except:
            messages.error(request, f'Info Not Saved, Check you inputs and try again!')

        return redirect('teams_page', id=dpt)


# Job Titles'
@log_activity
def add_new_title(request):
    if request.method == "POST":
        job_title = request.POST["job_title"]
        pos = request.POST["positions"]
        type = request.POST.get('type')
        salary = request.POST.get('salary')
        currency_id = request.POST.get('currency')
        description = request.POST.get('description')

        currency = get_currency(currency_id)

    try:
        job = Position(name=job_title, number_of_slots=pos, type=type, salary=salary,
                       currency=currency, description=description)
        job.save()
        messages.success(request, f'Info Successfully Saved')
        return redirect('job_titles_page')

    except:
        messages.error(request, f'Information Not Saved, Check you inputs and try again!')

    return redirect('job_titles_page')


def edit_job_title_page(request, id):
    context = {
        "user": request.user,
        "employee": get_active_employees(),
        "title": get_position(id),
    }
    return render(request, 'employees/edit_job_title.html', context)


@log_activity
def edit_job_title(request, id):
    try:
        if request.method == "POST":
            job = get_position(id)
            job.save()
            messages.success(request, f'Job Info Updated Successfully')
            return redirect('job_titles_page')
        else:
            messages.error(request, f'Update NOT Successfull')
            context = {
                "employees_page": "active",
            }
            return render(request, "employees/job_titles.html", context)
    except:
        messages.error(request, f'Info Not Saved, Check you inputs and try again!')
    return redirect('job_titles_page')


@log_activity
def delete_job_title(request, id):
    try:
        job = get_position(id)
        job.delete()
        messages.success(request, f'Job Title Deleted Successfully')
        return redirect('job_titles_page')
    except Department.DoesNotExist:
        messages.error(request, f'The Job Title no longer exists on the system')

    return redirect('job_titles_page')
