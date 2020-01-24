# Class for employee payroll
from employees.models import Employee


def convert_to_zero_if_none(value):
    if value:
        return int(value)
    else:
        return 0


def calculate_employee_nssf_contribution(gross_salary):
    nssf_contribution = 0.05 * gross_salary
    return nssf_contribution


def calculate_employer_nssf_contribution(gross_salary):
    nssf_contribution = 0.10 * gross_salary
    return nssf_contribution


def calculate_paye(gross_salary, currency_cost):
    # Assume the base currency is Uganda Shillings

    paye = 0.3 * (gross_salary - (410000 / currency_cost)) + (25000 / currency_cost)
    return paye


def get_sacco_deduction_amount(employee):
    deduction = employee.deduction_set.filter(name="Sacco").first()
    if deduction:
        sacco_deduction = convert_to_zero_if_none(deduction.amount)
        return sacco_deduction
    else:
        return 0


def get_damage_deduction_amount(employee):
    deduction = employee.deduction_set.filter(name="Damage").first()
    if deduction:
        damage_deduction = convert_to_zero_if_none(deduction.amount)
        return damage_deduction
    else:
        return 0


class SimplePayslip:

    def __init__(self, employee: Employee, overtime_pay=None, bonus=None):
        self.employee = employee
        self.overtime_pay = convert_to_zero_if_none(overtime_pay)
        self.bonus = convert_to_zero_if_none(bonus)
        self.gross_salary = self.sum_all_income(employee)
        self.employee_nssf = calculate_employee_nssf_contribution(self.gross_salary)
        self.employer_nssf = calculate_employer_nssf_contribution(self.gross_salary)
        self.currency_cost = int(self.employee.currency.cost)
        self.paye = calculate_paye(self.gross_salary, self.currency_cost)
        self.sacco_deduction_amount = get_sacco_deduction_amount(employee)
        self.damage_deduction_amount = get_damage_deduction_amount(employee)
        self.total_deductions = self.total_statutory_deductions + self.total_non_statutory_deductions
        self.lunch_allowance = int(self.employee.lunch_allowance/self.currency_cost)

    def sum_all_income(self, employee):
        return employee.initial_gross_salary + self.overtime_pay + self.bonus

    @property
    def total_nssf_deduction(self):
        return self.employee_nssf + self.employer_nssf

    @property
    def total_statutory_deductions(self):
        return self.employee_nssf + self.paye

    @property
    def total_non_statutory_deductions(self):
        return self.sacco_deduction_amount + self.damage_deduction_amount

    @property
    def net_salary(self):
        return self.gross_salary - self.total_deductions
