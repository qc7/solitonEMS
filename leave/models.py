from django.db import models
from django.utils import timezone

class Leave_Types(models.Model):
    leave_type = models.CharField(max_length=45)
    leave_days = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.leave_type

class Holidays(models.Model):
    holiday_date = models.DateField()
    holiday_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=15)

class Approval_Path(models.Model):
    path_name = models.CharField(max_length=45)
    required = models.BooleanField()
    first_approval = models.CharField(max_length=45)
    second_approval = models.CharField(max_length=45)
    third_approval = models.CharField(max_length=45)
    fourth_approval =models.CharField(max_length=45)

class LeaveApplication(models.Model):
    Employee_Name =models.CharField(max_length=60)
    leave_type = models.ForeignKey(Leave_Types, on_delete=models.CASCADE)
    apply_date=models.DateField(default=timezone.now)
    start_date = models.DateField()
    end_date=models.DateField()
    supervisor=models.CharField(max_length=45, default="")
    sup_Status=models.CharField(max_length=15, default="Pending")
    hod=models.CharField(max_length=45, default="")
    hod_status = models.CharField(max_length=15, default="Pending")
    hr=models.CharField(max_length=45, default="")
    hr_status = models.CharField(max_length=15, default="Pending")
    app_status = models.CharField(max_length=10, default="Pending")
    remarks = models.TextField()