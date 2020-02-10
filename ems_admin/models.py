from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class EMSPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    module = models.CharField(max_length=20, blank=True)
    full_auth = models.BooleanField(default=True)
    view_only = models.BooleanField(default=True)

    def __str__(self):
        return "%s permission" % self.name
