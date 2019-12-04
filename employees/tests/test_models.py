from django.test import TestCase
from employees.models import Employee, Department, Position, OrganisationDetail
from django.utils import timezone
from settings.models import Currency


class TestModel(TestCase):
    def setUp(self):
        currency = Currency.objects.create(
            code="UGX"
        )
        employee = Employee.objects.create(
            first_name="Test",
            last_name="Employee",
            start_date=timezone.now().today(),
            dob=timezone.now().today(),
            currency=currency
        )
        department = Department.objects.create(
            name="Testing Department",
            hod="Testing Master",
            status="Active"
        )

        position = Position.objects.create(
            name="Testing Engineer",
            number_of_slots=3
        )
        self.organisation_detail = OrganisationDetail.objects.create(
            employee=employee,
            department=department,
            position=position
        )

    def test_organisation_detail_model(self):
        self.assertEquals(self.organisation_detail.position.name, "Testing Engineer")
