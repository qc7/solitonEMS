from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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

    
class Leave(models.Model):
    Employee_Name =models.CharField(max_length=60)
    designation = models.CharField(max_length=20)
    nin = models.CharField(max_length=30)
    department=models.CharField(max_length=15)
    apply_date=models.DateField()
    _year=models.CharField(max_length=4)
    start_date = models.DateField()
    end_date=models.DateField()
    supervisor=models.CharField(max_length=45)
    sup_Status=models.CharField(max_length=15)
    hod=models.CharField(max_length=45)
    hod_status = models.CharField(max_length=15)
