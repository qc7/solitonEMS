from overtime.models import OvertimeApplication


def get_overtime_application(id):
    return OvertimeApplication.objects.get(pk=id)


def get_hod_pending_overtime_applications(user):
    hod_department = user.solitonuser.employee.department
    # Get the pending overtime applications for the particular hod department
    pending_applications = OvertimeApplication.objects.filter(status="Pending", HOD_approval="Pending")
    hod_pending_applications = []
    for pending_application in pending_applications:
        if pending_application.supervisee.department == hod_department:
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
                                                              HOD_approval="Approved")
    return pending_applications
