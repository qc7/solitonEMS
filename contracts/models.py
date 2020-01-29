from django.db import models

# Create your models here.
from employees.models import Position, Employee


class Contract(models.Model):
    reference_number = models.IntegerField(unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    effective_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=10, default="Active")
    risk = models.CharField(max_length=10)
    document = models.FileField()

    def __str__(self):
        return "Contract {}".format(str(self.reference_number))
