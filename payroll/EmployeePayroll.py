# Class for employee payroll
class EmployeePayroll:
    #
    lunch_allowance = 150000

    def __init__(self,basic_salary):
        self.basic_salary = basic_salary
        self.gross_salary = self.basic_salary + self.lunch_allowance
        self.nssf_contrib = 0.05*self.gross_salary
        self.employer_nssf_contrib = 0.10*self.gross_salary
        self.paye = 0.3*(self.gross_salary-410000)+25000
        self.net_salary = self.gross_salary - (self.nssf_contrib + self.paye)
        self.hourly_rate = (float(self.gross_salary)/26.0)/8
        self.daily_rate = (float(self.gross_salary)/26.0)

    def add_allowance(self,amount):
        self.gross_salary = self.gross_salary + amount

    def deduct(self,amount):
        self.net_salary = self.net_salary - amount

    def add_bonus(self,amount):
        self.bonus = amount
        self.gross_salary = self.gross_salary + self.bonus

    def add_half_bonus(self):
        self.bonus = 0.5 * self.basic_salary

    def add_overtime(self,hours_worked,holiday):
        if holiday:
            self.overtime = hours_worked * 2 * self.hourly_rate
            self.gross_salary = float(self.gross_salary) + self.overtime
        else:
            self.overtime = hours_worked * 1.5 * self.hourly_rate
            self.gross_salary = float(self.gross_salary) + hours_worked * 1.5 * self.hourly_rate

    def add_prorate(self,days_worked):
        self.prorate = days_worked * self.daily_rate
        self.basic_salary = self.prorate
