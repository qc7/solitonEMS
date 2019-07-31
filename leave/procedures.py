from .models import LeaveApplication
from django.db.models import Sum

def get_leave_balance(employee, l_type):
    leave_balance = 0
    days_taken = LeaveApplication.objects.filter\
        (employee_id = employee, leave_type = l_type).aggregate(Sum('no_of_days'))
        
    total_days_taken = days_taken['no_of_days__sum']

    if total_days_taken is not None:
        leave_balance = l_type.leave_days - (int(total_days_taken))
    else:
        leave_balance = l_type.leave_days

    return leave_balance

def get_employee_leave(employee):
    leave_days = 0
    days_taken = LeaveApplication.objects.filter\
        (employee_id = employee, leave_type = 4).aggregate(Sum('no_of_days'))
        
    total_days_taken = days_taken['no_of_days__sum']

    if total_days_taken is None:
        leave_days = 0
    else:
        leave_days = int(total_days_taken)

    return leave_days

def leave_balance(employee):
    days_taken = get_employee_leave(employee)
    leave_balance = 21 - int(days_taken)

    return leave_balance