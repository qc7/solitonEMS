from employees.models import Employee
from payroll.simple_payslip import SimplePayslip
from payroll.models import Payslip
from payroll.procedures import get_total_non_statutory_deductions, get_overtime_pay


def create_payslip_list_service(payroll_record, bonus=None):
    list_of_payslips = []
    employees = Employee.objects.all()

    for employee in employees:
        overtime_pay = get_overtime_pay(employee)
        payslip = create_payslip_service(employee, payroll_record, bonus=bonus, overtime_pay=overtime_pay)
        list_of_payslips.append(payslip)

    return list_of_payslips


def create_payslip_service(employee: object, payroll_record: object, overtime_pay: object = None,
                           bonus: object = None) -> object:

    simple_payslip = SimplePayslip(employee, overtime_pay=overtime_pay, bonus=bonus)
    payslip = Payslip.objects.create(
        employee=employee,
        payroll_record=payroll_record,
        employee_nssf=simple_payslip.employee_nssf,
        employer_nssf=simple_payslip.employer_nssf,
        gross_salary=simple_payslip.gross_salary,
        net_salary=simple_payslip.net_salary,
        paye=simple_payslip.paye,
        total_nssf_contrib=simple_payslip.total_nssf_deduction,
        overtime=simple_payslip.overtime_pay,
        bonus=simple_payslip.bonus,
        sacco_deduction=simple_payslip.sacco_deduction_amount,
        damage_deduction=simple_payslip.damage_deduction_amount,
    )

    return payslip


