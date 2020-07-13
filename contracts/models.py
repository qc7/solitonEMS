from django.db import models

# Create your models here.
from employees.models import Employee
from organisation_details.models import Position


class Contract(models.Model):
    reference_number = models.IntegerField(unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type = models.CharField(max_length=40)
    effective_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=10, default="Active")
    risk = models.CharField(max_length=10)
    document = models.FileField(upload_to="contracts")

    def __str__(self):
        return "Contract {}".format(str(self.reference_number))
