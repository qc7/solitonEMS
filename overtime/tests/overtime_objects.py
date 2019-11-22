from django.utils import timezone

from employees.models import Employee
from overtime.models import OvertimeApplication


def get_supervisee(currency):
    supervisee = Employee.objects.create(
        first_name="Test",
        last_name="Employee",
        start_date=timezone.now().today(),
        dob=timezone.now().today(),
        currency=currency
    )
    return supervisee


def get_applicant(currency):
    supervisor: object = Employee.objects.create(
        first_name="Test",
        last_name="Supervisor",
        start_date=timezone.now().today(),
        dob=timezone.now().today(),
        currency=currency
    )
    return supervisor


def get_overtime_application(currency, HOD_approval="Pending", cfo_approval="Pending", ceo_approval="Pending"):
    overtime_application = OvertimeApplication.objects.create(
        status="Pending",
        date=timezone.now().today(),
        start_time=timezone.now(),
        end_time=timezone.now(),
        HOD_approval=HOD_approval,
        cfo_approval=cfo_approval,
        ceo_approval=ceo_approval,
        description="Testing overtime application",
        applicant=get_applicant(currency),
        supervisor=get_supervisee(currency)
    )
    return overtime_application
