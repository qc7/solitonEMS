from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    start_date    = models.DateField()
    marital_status = models.CharField(max_length=10)
    dob     = models.DateField()
    nationality = models.CharField(max_length=20)
    nssf_no = models.CharField(max_length=20)
    telephone_no = models.CharField(max_length=20)
    residence_address = models.CharField(max_length=20)
    national_id   = models.CharField(max_length=20)
    ura_tin = models.CharField(max_length=20)
    image_url = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

    
    