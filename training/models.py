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
    business_case = models.TextField(blank=True)
    objectives = models.TextField(blank=True)
    preparations = models.TextField(blank=True)
    skills = models.CharField(max_length=40, blank=True)
    knowledge = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    currency = models.ForeignKey(Currency, blank=True, on_delete=models.CASCADE)
    supervisor_approval = models.CharField(max_length=10, default="Pending")
    HOD_approval = models.CharField(max_length=10, default="Pending")
    HR_approval = models.CharField(max_length=10, default="Pending")
    cfo_approval = models.CharField(max_length=10, default="Pending")
    ceo_approval = models.CharField(max_length=10, default="Pending")
    status = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return self.programme


class TrainingSchedule(models.Model):
    programme = models.CharField(max_length=30)
    duration = models.IntegerField()
    venue = models.CharField(max_length=40)
    purpose = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.programme