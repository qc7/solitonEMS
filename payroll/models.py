from django.db import models
from employees.models import Employee
# Create your models here.

class PayrollRecord(models.Model):
    year = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    
    def __str__(self):
        return self.month + " " + self.year
        
class Payroll(models.Model):
    employee   =    models.ForeignKey(Employee,on_delete=models.CASCADE,default="")
    payroll_record = models.ForeignKey(PayrollRecord,on_delete=models.CASCADE, default="")
    employee_nssf =  models.CharField(max_length=15)
    employer_nssf =  models.CharField(max_length=15)
    gross_salary    =   models.CharField(max_length=15,default="")
    net_salary      =   models.CharField(max_length=15,default="")
    paye = models.CharField(max_length=20)

    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name

