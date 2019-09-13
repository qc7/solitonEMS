from django.db import models
from django.contrib.auth.models import User
from employees.models import Employee

# Create your models here.
class SolitonUser(models.Model):
    # This line is required. Links SolitonUser to a User model instance
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # The additional attributes we wish to include
    middleName = models.CharField(max_length=20, blank=True)
    employee   = models.OneToOneField(Employee,on_delete=models.CASCADE,default=0)
    is_hod = models.CharField(max_length=10,default='False')
    is_hr  = models.CharField(max_length=10,default='False')
    is_cfo  = models.CharField(max_length=10, default='False')
    is_ceo  = models.CharField(max_length=10,default="False")
    password_change =models.CharField(max_length=10,blank=True)
    # Return something meaningful 
    def __str__(self):
        return '{}'.format(self.user.username)

# Stores all the notifications
class Notification(models.Model):
    user = models.ForeignKey(SolitonUser,on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,default='unread')

    def __str__(self):
        return '{} {} {}'.format(self.user, self.message,self.date_time)

