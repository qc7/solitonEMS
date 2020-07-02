from organisation_details.models import Department, Team, Position, OrganisationDetail
from organisation_details.models import Department, Position, OrganisationDetail, Team


def get_all_departments():
    return Department.objects.all()


def get_all_positions():
    return Position.objects.all()


def get_position(position_id):
    return Position.objects.get(pk=position_id)


def get_organisationdetail(user):
    try:
        organisationdetail = user.solitonuser.employee.organisationdetail
        return organisationdetail
    except:
        return None


def get_department(department_id):
    return Department.objects.get(pk=department_id)


def get_department_instance(employee):
    """Get employee department"""
    return employee.organisationdetail.department


def get_team_instance(employee):
    """Get employee team"""
    return employee.organisationdetail.team


def get_all_teams():
    return Team.objects.all()


def get_all_teams():
    return Team.objects.all()


def get_team(team_id):
    return Team.objects.get(pk=team_id)


def get_is_supervisor_in_team(approver):
    """Determine whether the approver is a supervisor in their team"""
    employee = approver.solitonuser.employee
    team = get_team_instance(employee)
    return employee.id is team.supervisor.id


def get_is_hod_in_department(approver):
    """Determine whether the approver is HOD in their department"""
    employee = approver.solitonuser.employee
    department = get_department_instance(employee)
    return employee.id is department.hod.id
