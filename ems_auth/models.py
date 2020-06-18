from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from employees.models import Employee


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_hod = models.BooleanField(default=False)
    is_hr = models.BooleanField(max_length=10, default=False)
    is_cfo = models.BooleanField(default=False)
    is_ceo = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    password_changed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    # Return something meaningful
    def __str__(self):
        return '{}'.format(self.email)

    @property
    def status(self):
        if self.is_active:
            return 'Active'
        else:
            return 'Inactive'

    @property
    def get_unread_notifications(self):
        return self.notification_set.filter(status="Unread")

    class Meta:
        unique_together = ['email']


class SolitonUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
