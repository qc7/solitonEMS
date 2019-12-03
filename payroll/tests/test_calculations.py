from django.test import TestCase

from payroll.calculations import calculate_overtime
from payroll.tests.payroll_objects import create_test_employee_object


class TestCalculation(TestCase):
    def setUp(self):
        self.employee = create_test_employee_object()

    def test_calculate_overtime(self):
        self.assertIsInstance(calculate_overtime(self.employee),int)