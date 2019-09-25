from django.db.models import QuerySet
from django.test import TestCase

from employees.models import Employee
from overtime.models import OvertimeApplication
from overtime.selectors import get_cfo_pending_overtime_applications, get_ceo_pending_overtime_applications
from overtime.tests.overtime_objects import get_supervisor, get_supervisee, get_overtime_application

from settings.models import Currency


class TestSelector(TestCase):
    def setUp(self):
        currency = Currency.objects.create(
            code="UGX"
        )
        overtime_app1 = get_overtime_application(currency, HOD_approval="Approved")
        overtime_app2 = get_overtime_application(currency, HOD_approval="Approved")
        overtime_app3 = get_overtime_application(currency,HOD_approval="Approved",cfo_approval="Approved")
        overtime_app4 = get_overtime_application(currency, HOD_approval="Approved", cfo_approval="Approved")

    def test_get_cfo_pending_overtime_applications(self):
        self.assertIsInstance(get_cfo_pending_overtime_applications(), QuerySet, msg=None)
        self.assertEquals(get_cfo_pending_overtime_applications().count(),2)

    def test_get_ceo_pending_overtime_applications(self):
        self.assertIsInstance(get_ceo_pending_overtime_applications(),QuerySet)
        self.assertEqual(get_ceo_pending_overtime_applications().count(),2)
