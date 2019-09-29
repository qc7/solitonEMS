from django.test import TestCase

from payroll.services import create_payslip_list_service, create_payslip_service
from payroll.tests.payroll_objects import create_test_payroll_record_object, create_test_employee_object


class TestService(TestCase):
    def setUp(self):
        self.payroll_record = create_test_payroll_record_object()
        self.employee = create_test_employee_object()
        self.payslip = create_payslip_service(self.employee,self.payroll_record)

    def test_create_payslip_list_service(self):
        self.assertIsInstance(create_payslip_list_service(self.payroll_record), list)

    def test_create_payslip_service(self):
        self.assertEqual(self.payslip.net_salary, 845500)
