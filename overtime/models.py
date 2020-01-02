from django.db import models
from django.utils import timezone

from employees.models import Employee


# Create your models here.


class OvertimeApplication(models.Model):
    status = models.CharField(max_length=10, default="Pending")
    date = models.DateField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    supervisor_approval = models.CharField(max_length=10, default="Pending")
    HOD_approval = models.CharField(max_length=10, default="Pending")
    HR_approval = models.CharField(max_length=10, default="Pending")
    cfo_approval = models.CharField(max_length=10, default="Pending")
    ceo_approval = models.CharField(max_length=10, default="Pending")
    applicant = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='supervisor', blank=True)

    def __str__(self):
        return "{}'s overtime {} {}".format(self.applicant.first_name, self.start_time, self.end_time)

    @property
    def number_of_hours(self):
        duration = self.end_time - self.start_time
        return round(duration.total_seconds() / 3600)
