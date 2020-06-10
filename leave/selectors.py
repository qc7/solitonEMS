from django.contrib.auth import get_user_model

from .models import LeaveApplication

user = get_user_model()

def get_supervisor_users(applicant):
    team = applicant.team

    all_supervisor_users = user.objects.filter(is_supervisor=True)
    users = []
    for supervisor_user in all_supervisor_users:
        if supervisor_user.solitonuser.employee.team == team:
            users.append(supervisor_user)

    return users

def get_hod_users(applicant):
    department = applicant.department

    all_hod_users = user.objects.filter(is_hod=True)
    users = []
    for hod_user in all_hod_users:
        if hod_user.solitonuser.employee.department == department:
            users.append(hod_user)

    return users

def get_hr_users():
    all_hr_users = user.objects.filter(is_hr=True)
    return all_hr_users
