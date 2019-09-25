from django.test import TestCase
from django.contrib.auth.models import User
from employees.models import Employee
from role.models import SolitonUser
from settings.models import Currency
from django.utils import timezone


class TestModel(TestCase):
    def setUp(self):
        currency = Currency.objects.create(
            code= "UGX"
        )
        user = User.objects.create_user(username="test_user",password="solitonug")
        employee = Employee.objects.create(
            first_name = "Test",
            last_name = "Employee",
            start_date = timezone.now().today(),
            dob = timezone.now().today(),
            currency = currency
        )
        self.solitonuser = SolitonUser.objects.create(
            user = user,
            employee = employee
        )

    def test_if_solitonuser_has_username(self):
        self.assertEquals(self.solitonuser.user.username, "test_user")