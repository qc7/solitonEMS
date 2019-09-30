from django.db.models import QuerySet, Sum

from employees.models import Employee
from overtime.selectors import get_approved_overtime_applications


def calculate_overtime(employee: Employee) -> int:
    # Get all approved overtime applications for the employee
    approved_overtime_applications: QuerySet = get_approved_overtime_applications(employee)
    # If employee has overtime applications continue if not return zero
    if approved_overtime_applications:
        # Sum the overtime pay for each overtime application

        # Return the overtime pay
        return total_overtime_pay
    else:
        return 0
