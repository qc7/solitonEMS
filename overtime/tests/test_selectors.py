from django.db.models import QuerySet
from django.test import TestCase

from overtime.selectors import get_cfo_pending_overtime_applications, get_ceo_pending_overtime_applications, \
    get_approved_overtime_applications
from overtime.tests.overtime_objects import get_applicant, get_supervisee, get_overtime_application
from payroll.tests.payroll_objects import create_test_employee_object

from settings.models import Currency


class TestSelector(TestCase):
    def setUp(self):
        currency = Currency.objects.create(
            code="UGX"
        )
        self.employee = get_applicant(currency)
        self.overtime_app1 = get_overtime_application(currency, HOD_approval="Approved")
        overtime_app2 = get_overtime_application(currency, HOD_approval="Approved")
        overtime_app3 = get_overtime_application(currency,HOD_approval="Approved",cfo_approval="Approved")
        overtime_app4 = get_overtime_application(currency, HOD_approval="Approved", cfo_approval="Approved")

    def test_get_cfo_pending_overtime_applications(self):
        self.assertIsInstance(get_cfo_pending_overtime_applications(), QuerySet, msg=None)
        self.assertEquals(get_cfo_pending_overtime_applications().count(),2)

    def test_get_ceo_pending_overtime_applications(self):
        self.assertIsInstance(get_ceo_pending_overtime_applications(),QuerySet)
        self.assertEqual(get_ceo_pending_overtime_applications().count(),2)

    def test_get_all_approved_overtime_applications_for_employee(self):
        self.assertIsInstance(get_approved_overtime_applications(self.employee),QuerySet)

    def test_number_of_hours(self):
        self.assertEqual(self.overtime_app1.number_of_hours,0)
