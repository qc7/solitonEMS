from django.db.models import Sum

def get_total_deduction(employee):
    total_deduction = 0
    if employee.deduction_set.all():
        sum = employee.deduction_set.aggregate(Sum('amount'))
        total_deduction = sum['amount__sum']
        return total_deduction