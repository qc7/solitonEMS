from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from employees.models import Employee
from employees.selectors import get_active_employees
from ems_auth.decorators import hr_required, ems_login_required
from organisation_details.models import Position, Department, Team
from organisation_details.selectors import get_all_departments, get_department, get_position, get_all_positions
from settings.selectors import get_all_currencies, get_currency


def about_us(request):
    return render(request, "organisation_description.html")


def no_organisation_detail_page(request):
    context = {
        "organisation_detail_page": "active"
    }
    return render(request, 'no_organisation_detail.html', context)


@hr_required
def departments_page(request):
    context = {
        "user": request.user,
        "organisation_page": "active",
        "departs": get_all_departments(),
        "emps": get_active_employees(),
    }

    return render(request, "employees/departments.html", context)


@hr_required
def teams_page(request, id):
    user = request.user
    ts = Team.objects.filter(department=id)
    context = {
        "user": user,
        "employees_page": "active",
        "teams": ts,
        "dep": get_department(id),
        "emps": get_active_employees(),

    }

    return render(request, "employees/teams.html", context)


@ems_login_required
@hr_required
def job_titles_page(request):

    context = {
        "user": request.user,
        "organisation_page": "active",
        "positions": get_all_positions(),
        "currencies": get_all_currencies()
    }

    return render(request, "employees/job_titles.html", context)


# Department Section
def add_new_department(request):
    if request.method == "POST":
        dep_name = request.POST["dep_name"]
        hod = request.POST["hod"]

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
            department.save()
            messages.success(request, f'Department Infor Updated Successfully')
            return redirect('departments_page')

        else:
            messages.error(request, f'Update NOT Successfull')
            context = {
                "employees_page": "active",
            }

            return render(request, "employees/departments.html", context)

    except:
        messages.error(request, f'Info Not Saved, Check you inputs and try again!')

        return redirect('departments_page')


def edit_department_page(request, id):
    user = request.user
    department = get_department(id)

    context = {
        "user": user,
        "employee": get_active_employees(),
        "deps": department,
    }
    return render(request, 'employees/departments.html', context)


def delete_department(request, id):
    try:
        department = get_department(id)
        department.delete()
        messages.success(request, f'Department Deleted Successfully')
        return redirect('departments_page')
    except Department.DoesNotExist:
        messages.error(request, f'The department no longer exists on the system')
        return redirect('departments_page')


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


# Job Titles
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
    return render(request, 'employees/job_titles.html', context)


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


def delete_job_title(request, id):
    try:
        job = get_position(id)
        job.delete()
        messages.success(request, f'Job Title Deleted Successfully')
        return redirect('job_titles_page')
    except Department.DoesNotExist:
        messages.error(request, f'The Job Title no longer exists on the system')
        return redirect('job_titles_page')
