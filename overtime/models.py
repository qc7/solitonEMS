from django.db import models
from employees.models import Employee
# Create your models here.


class OvertimeApplication(models.Model):
    status = models.CharField(max_length=10,default="Pending")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    supervisor_approval = models.CharField(max_length=10,default="False")
    HOD_approval = models.CharField(max_length=10,default="False")
    HR_approval = models.CharField(max_length=10,default="False")
    applicant = models.ForeignKey(Employee,on_delete=models.CASCADE)