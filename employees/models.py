from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=45)
    hod = models.CharField(max_length=45)
    status = models.CharField(max_length=15, default="Active")

    def __str__(self):
        return self.name

class Teams(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    supervisors = models.CharField(max_length=45)
    status = models.CharField(max_length=15,default="Active")

class Job_Titles(models.Model):
    title = models.CharField(max_length=45)
    positions = models.IntegerField()

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    basic_salary    =   models.CharField(max_length=20,default="")
    grade = models.CharField(max_length=3,default="")
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
    image_url = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name

class OrganisationDetail(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE,blank=True)
    position = models.ForeignKey(Job_Titles, on_delete=models.CASCADE,blank=True)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, default=1,blank=True)
    def __str__(self):
        return self.position.title + " " + self.department.name



class HomeAddress(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE,primary_key=True)
    district = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    county =   models.CharField(max_length=20)
    sub_county = models.CharField(max_length=20)
    parish = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.district

class Certification(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year_completed = models.CharField(max_length=4)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class EmergencyContact(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    relationship = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=50)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Beneficiary(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    relationship = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=40)
    percentage = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Spouse(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    national_id = models.CharField(max_length=40)
    dob     = models.DateField()
    occupation = models.CharField(max_length=40)
    telephone = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    passport_number = models.CharField(max_length=40)
    alien_certificate_number = models.CharField(max_length=40)
    immigration_file_number = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Dependant(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    dob = models.DateField()
    gender = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.name

class Deduction(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return self.name + " " + str(self.amount)

class Leave(models.Model):
    Employee =models.ForeignKey(Employee, on_delete = models.CASCADE)
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

class BankDetail(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    name_of_bank = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.name_of_bank,self.bank_account)