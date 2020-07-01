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


def get_all_teams():
    return Team.objects.all()


def get_all_teams():
    return Team.objects.all()


def get_team(team_id):
    return Team.objects.get(pk=team_id)
