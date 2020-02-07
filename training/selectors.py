from training.models import Training, TrainingSchedule


def get_all_trainings():
    return Training.objects.all()


def get_all_training_schedules():
    return TrainingSchedule.objects.all()


def get_applicant_trainings(applicant):
    return Training.objects.filter(applicant=applicant)


def get_training_schedule(training_schedule_id):
    training_schedule = TrainingSchedule.objects.get(pk=training_schedule_id)
    return training_schedule


def get_hod_pending_training_applications(hod_department):
    # Get the pending overtime applications for the particular hod department
    pending_applications = Training.objects.filter(status="Pending", HOD_approval="Pending",
                                                   supervisor_approval="Approved")
    hod_pending_applications = []
    for pending_application in pending_applications:
        if pending_application.applicant.department == hod_department:
            hod_pending_applications.append(pending_application)
    return hod_pending_applications


def get_cfo_pending_training_applications():
    pending_applications = Training.objects.filter(status="Pending", cfo_approval="Pending",
                                                   HOD_approval="Approved")
    return pending_applications


def get_ceo_pending_training_applications():
    pending_applications = Training.objects.filter(status="Pending", cfo_approval="Approved",
                                                   ceo_approval="Pending")
    return pending_applications


def get_supervisor_pending_training_applications(supervisor):
    pending_applications = Training.objects.filter(supervisor_approval="Pending")
    return pending_applications


def get_hr_pending_training_applications():
    pending_applications = Training.objects.filter(HR_approval="Pending", HOD_approval="Approved",
                                                   status="Pending")
    return pending_applications


def get_pending_training_applications(approver):
    pending_applications = None

    if approver.is_supervisor:
        supervisor = approver.solitonuser.employee
        pending_applications = get_supervisor_pending_training_applications(supervisor)

    if approver.is_hod:
        hod_department = approver.solitonuser.employee.department
        pending_applications = get_hod_pending_training_applications(hod_department)

    if approver.is_hr:
        pending_applications = get_hr_pending_training_applications()

    if approver.is_cfo:
        pending_applications = get_cfo_pending_training_applications()

    if approver.is_ceo:
        pending_applications = get_ceo_pending_training_applications()

    return pending_applications


def get_training_application(training_application_id):
    return Training.objects.get(pk=training_application_id)
