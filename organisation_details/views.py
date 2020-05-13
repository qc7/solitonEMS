from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from employees.models import Employee
from employees.selectors import get_active_employees, get_employee
from ems_admin.decorators import log_activity
from ems_auth.decorators import hr_required, ems_login_required, organisation_full_auth_required
from organisation_details.models import Position, Department, Team
from organisation_details.selectors import get_all_departments, get_department, get_position, get_all_positions
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
@log_activity
def teams_page(request, id):
    ts = Team.objects.filter(department=id)
    context = {
        "user": request.user,
        "employees_page": "active",
        "teams": ts,
        "dep": get_department(id),
        "emps": get_active_employees(),

    }

    return render(request, "employees/teams.html", context)


@ems_login_required
@hr_required
@organisation_full_auth_required
@log_activity
def manage_job_positions_page(request):
    context = {
        "user": request.user,
        "organisation_page": "active",
        "positions": get_all_positions(),
        "currencies": get_all_currencies()
    }

    return render(request, "organisation_details/manage_job_positions.html", context)


# Department Section
@hr_required
@organisation_full_auth_required
@log_activity
def departments_page(request):
    context = {
        "user": request.user,
        "organisation_page": "active",
        "departments": get_all_departments(),
        "employees": get_active_employees(),
    }

    return render(request, "organisation_details/manage_departments.html", context)


@log_activity
def add_new_department(request):
    if request.method == "POST":
        department_name = request.POST["department_name"]
        employee_id = request.POST["employee_id"]
        employee = get_employee(employee_id)
        department = Department(name=department_name, hod=employee)
        department.save()
        messages.success(request, f'Info Successfully Saved')
        return redirect('manage_departments_page')

    return redirect('manage_departments_page')


def edit_department(request):

    if request.method == "POST":
        department_id = request.POST.get('department_id')
        employee_id = request.POST.get('employee_id')
        employee = get_employee(employee_id)
        department = get_department(department_id)
        department.name = request.POST.get('department_name')
        department.hod = employee
        department.save()
        return redirect('manage_departments_page')

    messages.error(request, f'Info Not Saved, Check you inputs and try again!')
    return redirect('manage_departments_page')


@log_activity
def edit_department_page(request, department_id):
    department = get_department(department_id)
    context = {
        "user": request.user,
        "employees": get_active_employees(),
        "department": department,
        "organisation_page": "active"
    }
    return render(request, 'organisation_details/edit_department.html', context)


@log_activity
def delete_department(request, department_id):
    try:
        department = get_department(department_id)
        department.delete()
        messages.success(request, f'Department Deleted Successfully')
        return redirect('manage_departments_page')
    except Department.DoesNotExist:
        messages.error(request, f'The department no longer exists on the system')

    return redirect('manage_departments_page')


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
def add_new_job_position(request):
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
        return redirect('manage_job_positions_page')

    except:
        messages.error(request, f'Information Not Saved, Check you inputs and try again!')

    return redirect('job_titles_page')


def edit_job_position_page(request, position_id):
    position = get_position(position_id)
    context = {
        "user": request.user,
        "position": position,
        "organisation_page": "active"

    }
    return render(request, 'organisation_details/edit_position.html', context)


@log_activity
def edit_job_position(request):
    if not request.POST:
        return redirect('manage_job_positions_page')

    position_id = request.POST.get('position_id')
    currency_id = request.POST.get('currency')
    currency = get_currency(currency_id)
    position = get_position(position_id)
    position.name = request.POST.get('name')
    position.number_of_slots = request.POST.get('number_of_slots')
    position.type = request.POST.get('type')
    position.salary = request.POST.get('salary')
    position.currency = currency
    position.description = request.POST.get('description')
    position.save()
    messages.success(request, "Job Position successfully edited")
    return redirect('manage_job_positions_page')


@log_activity
def delete_job_position(request, position_id):
    try:
        position = get_position(position_id)
        position.delete()
        messages.success(request, f'Job Position Deleted Successfully')
        return redirect('manage_job_positions_page')
    except Department.DoesNotExist:
        messages.error(request, f'The Job Position no longer exists on the system')

    return redirect('manage_job_positions_page')
