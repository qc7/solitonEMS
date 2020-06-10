from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives

from leave.selectors import get_supervisor_users
#, get_hr_users, get_hod_users, get_cfo_users, get_ceo_users
from SOLITONEMS.settings import BASE_DIR


def send_leave_application_email(approvers, leave_application, domain=None):
    approver_emails = []
    for approver in approvers:
        approver_emails.append(approver.email)

    context = {
        'applicant_name': leave_application.employee,
        'server_url': domain
    }
    
    subject, from_mail, to = 'New Leave Application', None, approver_emails
    html_content = get_template('email/application_notification.html').render(context)
    msg=EmailMultiAlternatives(subject,None, from_mail, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

def send_leave_response_email(leave_application, approver, status, domain=None):
    applicant = leave_application.employee
    user=applicant.solitonuser.user

    context = {
        'applicant':applicant,
        'leave_application': leave_application,
        'approver': approver,
        'status': status,
        'server_url': domain
    }
  
    subject, from_mail, to = 'Leave Application Response', None, user.email
    html_content = get_template('email/response_notification.html').render(context)
    msg=EmailMultiAlternatives(subject,None, from_mail, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()