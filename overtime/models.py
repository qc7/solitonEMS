from django.db import models
from employees.models import Employee
from holidays.selectors import is_on_holiday
from overtime.procedures import get_overtime_application_hours


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
        hours = get_overtime_application_hours(self.start_time, self.end_time)
        return round(hours, 2)

    @property
    def is_on_sunday(self):
        return self.start_time.weekday() == 6

    @property
    def is_on_holiday(self):
        return is_on_holiday(self.start_time)

    @property
    def overtime_pay(self):
        if self.is_on_holiday or self.is_on_sunday:
            overtime_amount = self.number_of_hours * 2 * self.applicant. \
                overtime_hourly_rate
            return int(overtime_amount)
        else:
            overtime_amount = self.number_of_hours * 1.5 * self.applicant. \
                overtime_hourly_rate
            return int(overtime_amount)


class OvertimePlan(models.Model):
    applicant = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True)
    date = models.DateField()
    HR_approval = models.CharField(max_length=10, default="Pending")
    cfo_approval = models.CharField(max_length=10, default="Pending")
    status = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return self.applicant


class OvertimeSchedule(models.Model):
    overtime_plan = models.ForeignKey(OvertimePlan, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
