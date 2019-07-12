# Class for employee payroll
class EmployeePayroll:
    #
    lunch_allowance = 150000
    prorate = 0
    def __init__(self,basic_salary):
        self.basic_salary = basic_salary
        self.get_gross_salary()
        self.get_nssf_contrib(self.gross_salary)
        self.get_employer_nssf_contrib(self.gross_salary)
        self.get_paye(self.gross_salary)
        self.get_net_salary(self.gross_salary)
        self.get_hourly_rate(self.gross_salary)
        self.get_daily_rate(self.gross_salary)    

    def get_gross_salary(self):
        self.gross_salary = int(self.basic_salary) + int(self.lunch_allowance) 
        return self.gross_salary
          
    def get_nssf_contrib(self,gross_salary):
        self.nssf_contrib = 0.05*gross_salary
        return self.nssf_contrib

    def get_employer_nssf_contrib(self,gross_salary):
        self.employer_nssf_contrib = 0.10*self.gross_salary
        return self.employer_nssf_contrib

    def get_paye(self,gross_salary):
        self.paye = 0.3*(self.gross_salary-410000)+25000
        return self.paye

    def get_net_salary(self,gross_salary):
        self.net_salary = int(gross_salary) - (self.nssf_contrib + self.paye)
        return self.net_salary

    def get_hourly_rate(self,gross_salary):
        self.hourly_rate = (float(self.gross_salary)/26.0)/8
        return self.hourly_rate

    def get_daily_rate(self,gross_salary):
        self.daily_rate = (float(gross_salary)/26.0)

    def add_allowance(self,amount):
        self.gross_salary = self.gross_salary + amount

    def deduct(self,amount):
        if amount is None:
            amount = 0

        self.net_salary = int(self.net_salary) - int(amount)

    def add_bonus(self,amount):
        self.bonus = amount
        self.gross_salary = int(self.gross_salary) + int(self.bonus)
        if self.prorate:
            self.gross_salary = self.prorate

        self.get_nssf_contrib(self.gross_salary)
        self.get_employer_nssf_contrib(self.gross_salary)
        self.get_paye(self.gross_salary)
        self.get_net_salary(self.gross_salary)
        self.get_hourly_rate(self.gross_salary)
        self.get_daily_rate(self.gross_salary) 

    def add_half_bonus(self):
        self.bonus = 0.5 * self.basic_salary

    def add_overtime_amount(self,amount):
        self.overtime = int(amount)
        self.gross_salary = self.gross_salary + self.overtime

    def add_overtime(self,hours_worked,holiday):
        if holiday:
            self.overtime = hours_worked * 2 * self.hourly_rate
            self.gross_salary = float(self.gross_salary) + self.overtime
            return self.overtime
        else:
            self.overtime = hours_worked * 1.5 * self.hourly_rate
            self.gross_salary = float(self.gross_salary) + hours_worked * 1.5 * self.hourly_rate
            return self.overtime
    
    def add_prorate_amount(self,amount):
        self.prorate = float(amount)

    def add_prorate(self,days_worked):
        self.prorate = float(days_worked) * self.daily_rate
        self.gross_salary = self.prorate
        self.get_nssf_contrib(self.gross_salary)
        self.get_employer_nssf_contrib(self.gross_salary)
        if self.gross_salary == 0:
            self.paye = 0

        self.get_net_salary(self.gross_salary)

    def set_gross_salary(self,amount):
        self.gross_salary = int(amount)

# employee_payroll = EmployeePayroll(1000000)
# employee_payroll.add_bonus(600000)
# print(employee_payroll.net_salary)