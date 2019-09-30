from django.test import TestCase

from payroll.selectors import get_payroll_by_id, get_payroll_record_by_id
from payroll.tests.payroll_objects import create_test_payslip_object, create_test_payroll_record_object


class TestSelector(TestCase):

    def setUp(self):
        self.payroll = create_test_payslip_object()
        self.payroll_record = create_test_payroll_record_object()

    def test_get_payroll_selector(self):
        self.assertEqual(get_payroll_by_id(1).id, 1)

    def test_get_payroll_record_selector(self):
        self.assertEqual(get_payroll_record_by_id(1).id,1)
