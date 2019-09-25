from django.db import models
from employees.models import Employee
# Create your models here.


class OvertimeApplication(models.Model):
    status = models.CharField(max_length=10,default="Pending")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    supervisor_approval = models.CharField(max_length=10,default="Pending")
    HOD_approval = models.CharField(max_length=10,default="Pending")
    HR_approval = models.CharField(max_length=10,default="Pending")
    cfo_approval = models.CharField(max_length=10,default="Pending")
    ceo_approval = models.CharField(max_length=10,default="Pending")
    supervisor = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,related_name='supervisee')
    supervisee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='supervisor',blank=True)



    def __str__(self):
        return "{}'s overtime {} {}".format(self.supervisee.first_name,self.start_time,self.end_time)