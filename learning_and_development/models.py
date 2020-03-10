from django.db import models

# Create your models here.
from organisation_details.models import Department


class Resource(models.Model):
    name = models.CharField(max_length=40)
    producer = models.CharField(max_length=40)
    file_format = models.CharField(max_length=10)
    year_published = models.IntegerField()
    department = models.ForeignKey(Department, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='resources')

    def __str__(self):
        return self.name


