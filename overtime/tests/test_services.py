from django.test import TestCase

from overtime.services import approve_overtime_application_finally
from overtime.tests.overtime_objects import get_overtime_application
from settings.models import Currency


class TestService(TestCase):
    def setUp(self):
        currency = Currency.objects.create(
            code="UGX"
        )
        overtime_application = get_overtime_application(currency)
        self.overtime_application_id = overtime_application.id

    def test_approve_overtime_application_finally_function(self):
        self.assertEquals(approve_overtime_application_finally(self.overtime_application_id).status, "Approved")


