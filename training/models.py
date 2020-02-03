from django.db import models

# Create your models here.
from employees.models import Employee
from settings.models import Currency


class Training(models.Model):
    applicant = models.ForeignKey(Employee, on_delete=models.CASCADE)
    programme = models.CharField(max_length=40)
    institution = models.CharField(max_length=40)
    duration = models.IntegerField()
    cost = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    business_case = models.TextField()
    objectives = models.TextField()
    preparations = models.TextField()
    skills = models.CharField(max_length=40)
    knowledge = models.TextField()
    comments = models.TextField()
    currency = models.ForeignKey(Currency, blank=True, on_delete=models.CASCADE)
    supervisor_approval = models.CharField(max_length=10, default="Pending")
    HOD_approval = models.CharField(max_length=10, default="Pending")
    HR_approval = models.CharField(max_length=10, default="Pending")
    cfo_approval = models.CharField(max_length=10, default="Pending")
    ceo_approval = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return self.programme
