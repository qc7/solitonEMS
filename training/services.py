from training.models import Training


def approve_overtime_application_finally(id):
    # Get the training application
    training_application = Training.objects.get(pk=id)
    training_application.status = "Approved"
    training_application.save()
    return training_application


def reject_finally(training_application):
    training_application.status = "Rejected"
    training_application.save()
    return training_application


def supervisor_reject(training_application):
    training_application.supervisor_approval = "Rejected"
    training_application.save()
    return training_application


def supervisor_approve(training_application):
    training_application.supervisor_approval = "Approved"
    training_application.save()
    return training_application


def hr_approve(training_application):
    training_application.HR_approval = "Approved"
    training_application.save()
    return training_application


def hr_reject(overtime_application):
    overtime_application.HR_approval = "Rejected"
    overtime_application.save()
    return overtime_application


def hod_reject(training_application):
    training_application.HOD_approval = 'Rejected'
    training_application.save()
    return training_application


def cfo_reject(training_application):
    training_application.cfo_approval = 'Rejected'
    training_application.save()
    return training_application


def ceo_reject(training_application):
    training_application.ceo_approval = 'Rejected'
    training_application.save()
    return training_application


def hod_approve(training_application):
    # Get the training application
    training_application.HOD_approval = 'Approved'
    training_application.save()
    return training_application


def cfo_approve(training_application):
    training_application.cfo_approval = 'Approved'
    training_application.save()
    return training_application


def ceo_approve(training_application):
    # Get the training application
    training_application.ceo_approval = 'Approved'
    training_application.status = "Approved"
    training_application.save()
    return training_application


def approve_training_application_service(approver, training_application):
    approved_training_application = None

    if approver.is_supervisor:
        approved_training_application = supervisor_approve(training_application)

    if approver.is_hod:
        approved_training_application = hod_approve(training_application)

    if approver.is_hr:
        approved_training_application = hr_approve(training_application)

    if approver.is_cfo:
        approved_training_application = cfo_approve(training_application)

    if approver.is_ceo:
        approved_training_application = ceo_approve(training_application)

    return approved_training_application


def reject_training_application_service(rejecter, training_application):
    if rejecter.is_supervisor:
        rejected_training_application = supervisor_reject(training_application)

    elif rejecter.is_hod:
        rejected_training_application = hod_reject(training_application)

    elif rejecter.is_hr:
        rejected_training_application = hr_reject(training_application)

    elif rejecter.is_cfo:
        rejected_training_application = cfo_reject(training_application)

    elif rejecter.is_ceo:
        rejected_training_application = ceo_reject(training_application)
    else:
        rejected_training_application = None

    return rejected_training_application
