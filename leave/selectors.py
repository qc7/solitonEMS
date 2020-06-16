from django.contrib.auth import get_user_model
import datetime

from .models import LeaveApplication, Leave_Records, Leave_Types


user = get_user_model()

# Leave Type Selectors
def get_all_leave_types():
    return Leave_Types.objects.all()

def get_leave_type(leave_type_id):
    return Leave_Types.objects.get(pk=leave_type_id)

# Leave Records Selectors
def get_all_leave_records():
    return Leave_Records.objects.all()

def get_leave_record(employee):
    try:
        leave_record = Leave_Records.objects.get(employee=employee, leave_year=datetime.date.today().year)
        return leave_record 
    except:
        return None

# Leave Application Selectors
def get_all_leave_applications():
    return LeaveApplication.objects.all()

def get_employee_leave_applications(employee):
    return LeaveApplication.objects.filter(employee=employee)

def get_leave_application(leave_application_id):
    return LeaveApplication.objects.get(pk=leave_application_id)


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
