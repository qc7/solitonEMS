# Class for employee payroll
class EmployeePayroll:
    lunch_allowance = 160000
    def __init__(self,basic_salary):
        self.basic_salary = basic_salary
        self.gross_salary = self.basic_salary + self.lunch_allowance
        self.nssf_contrib = 0.05*self.gross_salary
        self.employer_nssf_contrib = 0.10*self.gross_salary
        self.paye = 0
        self.net_salary = self.gross_salary - (self.nssf_contrib+self.paye)

    def add_allowance(self,amount):
        self.gross_salary = self.gross_salary + amount

    def deduct(self,amount):
        self.gross_salary = self.gross_salary - amount

employee = EmployeePayroll(10000000)
print(employee.lunch_allowance)