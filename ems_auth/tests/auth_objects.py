from django.utils import timezone

from employees.models import Employee


def get_employee(currency):
    employee = Employee.objects.create(
        first_name="Test",
        last_name="Employee",
        start_date=timezone.now().today(),
        dob=timezone.now().today(),
        currency=currency
    )
    return employee

