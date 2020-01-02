from employees.models import Employee
from overtime.models import OvertimeApplication


def get_overtime_application(id):
    return OvertimeApplication.objects.get(pk=id)


def get_hod_pending_overtime_applications(hod_department):
    # Get the pending overtime applications for the particular hod department
    pending_applications = OvertimeApplication.objects.filter(status="Pending", HOD_approval="Pending",
                                                              supervisor_approval="Approved")
    hod_pending_applications = []
    for pending_application in pending_applications:
        if pending_application.applicant.department == hod_department:
            hod_pending_applications.append(pending_application)
    return hod_pending_applications


def get_hod_approved_overtime_applications(user):
    hod_department = user.solitonuser.employee.department
    # Get the approved overtime applications for the particular hod department
    approved_applications = OvertimeApplication.objects.filter(status="Pending", HOD_approval="Approved")
    hod_pending_applications = []
    for approved_application in approved_applications:
        if approved_application.supervisee.department == hod_department:
            hod_pending_applications.append(approved_application)
    return hod_pending_applications


def get_cfo_pending_overtime_applications():
    pending_applications = OvertimeApplication.objects.filter(status="Pending", cfo_approval="Pending",
                                                              HOD_approval="Approved")
    return pending_applications


def get_ceo_pending_overtime_applications():
    pending_applications = OvertimeApplication.objects.filter(status="Pending", cfo_approval="Approved",
                                                              ceo_approval="Pending")
    return pending_applications


def get_approved_overtime_applications(employee: Employee):
    approved_applications = OvertimeApplication.objects.filter(status="Approved", applicant=employee)
    return approved_applications


def get_all_overtime_applications():
    overtime_applications = OvertimeApplication.objects.all()
    return overtime_applications


def get_supervisor_pending_overtime_applications(supervisor):
    pending_applications = OvertimeApplication.objects.filter(supervisor_approval="Pending")
    return pending_applications


def get_hr_pending_overtime_applications():
    pending_applications = OvertimeApplication.objects.filter(HR_approval="Pending", HOD_approval="Approved",
                                                              status="Pending")
    return pending_applications


def get_pending_overtime_applications(approver):
    pending_applications = None

    if approver.is_supervisor:
        supervisor = approver.solitonuser.employee
        pending_applications = get_supervisor_pending_overtime_applications(supervisor)

    if approver.is_hod:
        hod_department = approver.solitonuser.employee.department
        pending_applications = get_hod_pending_overtime_applications(hod_department)

    if approver.is_hr:
        pending_applications = get_hr_pending_overtime_applications()

    if approver.is_cfo:
        pending_applications = get_cfo_pending_overtime_applications()

    if approver.is_ceo:
        pending_applications = get_ceo_pending_overtime_applications()

    return pending_applications


def get_recent_overtime_applications(limit):
    return OvertimeApplication.objects.all().order_by('-id')[:limit]
