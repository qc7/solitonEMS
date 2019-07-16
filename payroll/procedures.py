from django.db.models import Sum

def get_total_deduction(employee):
    total_deduction = 0
    if employee.deduction_set.all():
        sum = employee.deduction_set.aggregate(Sum('amount'))
        total_deduction = sum['amount__sum']
        return total_deduction

def get_total_nssf(payrolls):
    sum = payrolls.aggregate(Sum('total_nssf_contrib'))
    total_nssf_contrib = sum['total_nssf_contrib__sum']
    return total_nssf_contrib

def get_total_paye(payrolls):
    sum = payrolls.aggregate(Sum('paye'))
    paye = sum['paye__sum']
    return paye

def get_total_gross_pay(payrolls):
    sum = payrolls.aggregate(Sum('gross_salary'))
    gross_salary = sum['gross_salary__sum']
    return gross_salary

def get_total_basic_pay(employees):
    sum = employees.aggregate(Sum('basic_salary'))
    basic_salary = sum['basic_salary__sum']
    return basic_salary

def get_total_net_pay(payrolls):
    sum = payrolls.aggregate(Sum('net_salary'))
    net_salary = sum['net_salary__sum']
    return net_salary

