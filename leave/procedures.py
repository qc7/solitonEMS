from .models import LeaveApplication
from django.db.models import Sum

def get_leave_balance(employee, l_type):
    leave_balance = 0
    days_taken = LeaveApplication.objects.filter\
        (Employee_Name = employee, leave_type = l_type).aggregate(Sum('no_of_days'))
        
    total_days_taken = days_taken['no_of_days__sum']

    leave_balance = l_type.leave_days - (int(total_days_taken))

    return leave_balance

# def approve_request(role):
