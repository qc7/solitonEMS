from django.utils import timezone

from employees.models import Employee
from payroll.models import PayrollRecord, Payslip
from settings.models import Currency


def create_test_currency_object():
    currency = Currency.objects.create(
        code="UGX"
    )
    return currency


def create_test_employee_object():
    currency = create_test_currency_object()
    employee = Employee.objects.create(
        basic_salary=1000000,
        first_name="Test",
        last_name="Employee",
        start_date=timezone.now().today(),
        dob=timezone.now().today(),
        currency=currency,
        lunch_allowance=150000,
    )
    return employee


def create_test_payroll_record_object():
    payroll_record = PayrollRecord.objects.create(
        year="2000",
        month="January"
    )
    return payroll_record


def create_test_payslip_object():
    employee = create_test_employee_object()
    payroll_record = create_test_payroll_record_object()
    payslip = Payslip.objects.create(
        employee=employee,
        payroll_record=payroll_record,
        employee_nssf=10000,
        employer_nssf=100000,
        gross_salary=1000000,
        net_salary=1000000,
        paye=100000,
        overtime=0,
        sacco_deduction=0,
        damage_deduction=0
    )

    return payslip
