from django.db import models
from ems_auth.models import User


# Create your models here.

# Stores all the notifications
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default='unread')
    number = models.IntegerField()
 
    def __str__(self):
        return '{} {} {}'.format(self.user, self.message, self.date_time)
