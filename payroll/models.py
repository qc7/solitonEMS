from django.db import models
from employees.models import Employee


# Create your models here.

class PayrollRecord(models.Model):
    year = models.CharField(max_length=20)
    month = models.CharField(max_length=20)

    def __str__(self):
        return self.month + " " + self.year


class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default="")
    payroll_record = models.ForeignKey(PayrollRecord, on_delete=models.CASCADE, default="")
    employee_nssf = models.FloatField()
    employer_nssf = models.FloatField()
    gross_salary = models.FloatField()
    net_salary = models.FloatField()
    paye = models.FloatField()
    total_nssf_contrib = models.FloatField(default=0)
    overtime = models.FloatField()
    bonus = models.FloatField(default=0)
    sacco_deduction = models.FloatField()
    damage_deduction = models.FloatField()
    prorate = models.CharField(max_length=20, default="0.0")

    def __str__(self):
        return self.employee.first_name + " " + self.employee.last_name

    @property
    def basic_salary(self):
        return self.employee.basic_salary

    @property
    def total_statutory(self):
        return self.total_nssf_contrib + self.paye


