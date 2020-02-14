from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from employees.models import Employee
from ems_auth.decorators import hr_required, ems_login_required
from organisation_details.models import Position, Department, Team
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
    user = request.user
    context = {
        "user": request.user,
        "organisation_page": "active",
        "departs": Department.objects.all(),
        "emps": Employee.objects.all(),
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
        "dep": Department.objects.get(pk=id),
        "emps": Employee.objects.all(),
    }

    return render(request, "employees/teams.html", context)


@ems_login_required
@hr_required
def job_titles_page(request):
    currencies = get_all_currencies()
    context = {
        "user": request.user,
        "organisation_page": "active",
        "positions": Position.objects.all(),
        "currencies": currencies
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
            department = Department.objects.get(pk=id)
            dep_name = request.POST["dep_name"]
            hod = request.POST["hod"]

            # department = Departments.objects.get(pk=id)#.update(name=dep_name, hod=hod)

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
        messages.error(request, f'Infor Not Saved, Check you inputs and try again!')

        return redirect('departments_page')


def edit_department_page(request, id):
    # redirect according to roles
    # If user is a manager
    user = request.user
    # If user is an employee
    if str(user.solitonuser.soliton_role) == 'Employee':
        return render(request, "role/employee.html")
    # If user is HOD
    if str(user.solitonuser.soliton_role) == 'HOD':
        return render(request, "role/hod.html")

    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    department = Department.objects.get(pk=id)

    context = {
        "user": user,
        "employee": Employee.objects.all(),
        "deps": department,
    }
    return render(request, 'employees/departments.html', context)


def delete_department(request, id):
    try:
        department = Department.objects.get(pk=id)

        department.delete()
        messages.success(request, f'Department Deleted Successfully')
        return redirect('departments_page')
    except Department.DoesNotExist:
        messages.error(request, f'The department no longer exists on the system')
        return redirect('departments_page')


# Team Section
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
            messages.error(request, f'Infor Not Saved, Check you inputs and try again!')

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
    # redirect according to roles
    # If user is a manager
    user = request.user
    # If user is an employee
    if str(user.solitonuser.soliton_role) == 'Employee':
        return render(request, "role/employee.html")
    # If user is HOD
    if str(user.solitonuser.soliton_role) == 'HOD':
        return render(request, "role/hod.html")

    # The line requires the user to be authenticated before accessing the view responses.
    if not request.user.is_authenticated:
        # if the user is not authenticated it renders a login page
        return render(request, 'registration/login.html', {"message": None})

    title = Position.objects.get(pk=id)

    context = {
        "user": user,
        "employee": Employee.objects.all(),
        "title": title,
    }
    return render(request, 'employees/job_titles.html', context)


def edit_job_title(request, id):
    try:
        if request.method == "POST":
            job = Position.objects.get(pk=id)
            title = request.POST["title"]
            positions = request.POST["positions"]

            job.save()

            messages.success(request, f'Job Infor Updated Successfully')
            return redirect('job_titles_page')

        else:
            messages.error(request, f'Update NOT Successfull')
            context = {
                "employees_page": "active",
            }

            return render(request, "employees/job_titles.html", context)

    except:
        messages.error(request, f'Infor Not Saved, Check you inputs and try again!')

        return redirect('job_titles_page')


def delete_job_title(request, id):
    try:
        job = Position.objects.get(pk=id)

        job.delete()
        messages.success(request, f'Job Title Deleted Successfully')
        return redirect('job_titles_page')
    except Department.DoesNotExist:
        messages.error(request, f'The Job Title no longer exists on the system')
        return redirect('job_titles_page')

