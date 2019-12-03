from django.test import TestCase

from payroll.simple_payslip import SimplePayslip
from payroll.tests.payroll_objects import create_test_employee_object


class TestSimplePayslip(TestCase):

    def setUp(self):
        employee = create_test_employee_object()

        self.simple_payslip = SimplePayslip(employee,overtime_pay=100000)

    def test_simple_payslip_overtime_pay(self):
        self.assertEqual(self.simple_payslip.overtime_pay, 100000)
