from employees.models import Employee


def get_employee(employee_id):
    return Employee.objects.get(pk=employee_id)


def get_active_employees():
    return Employee.objects.filter(status='Active')



