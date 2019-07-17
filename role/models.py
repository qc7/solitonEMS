from django.db import models
from django.contrib.auth.models import User
from employees.models import Employee

class SolitonRole(models.Model):
    #Soliton role attributes
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Create your models here.
class SolitonUser(models.Model):
    # This line is required. Links SolitonUser to a User model instance
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # The additional attributes we wish to include
    middleName = models.CharField(max_length=20, blank=True)
    employee   = models.OneToOneField(Employee,on_delete=models.CASCADE)
    soliton_role = models.ForeignKey(SolitonRole,on_delete=models.CASCADE)
    password_change =models.CharField(max_length=10,blank=True)
    # Return something meaningful 
    def __str__(self):
        return '{}'.format(self.user.username)