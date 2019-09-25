from django.test import TestCase

from overtime.services import approve_overtime_application_finally, reject_overtime_application_finally, \
    hod_reject_overtime_application, cfo_reject_overtime_application, ceo_reject_overtime_application, \
    hod_approve_overtime_application, cfo_approve_overtime_application, ceo_approve_overtime_application
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

    def test_reject_overtime_application(self):
        self.assertEquals(reject_overtime_application_finally(self.overtime_application_id).status, "Rejected")

    def test_hod_reject_overtime_application(self):
        self.assertEquals(hod_reject_overtime_application(self.overtime_application_id).HOD_approval, "Rejected")

    def test_cfo_reject_overtime_application(self):
        self.assertEquals(cfo_reject_overtime_application(self.overtime_application_id).cfo_approval, "Rejected")

    def test_ceo_reject_overtime_application(self):
        self.assertEquals(ceo_reject_overtime_application(self.overtime_application_id).ceo_approval, "Rejected")

    def test_hod_approve_overtime_application(self):
        self.assertEquals(hod_approve_overtime_application(self.overtime_application_id).HOD_approval, "Approved")

    def test_cfo_approve_overtime_application(self):
        self.assertEquals(cfo_approve_overtime_application(self.overtime_application_id).cfo_approval, "Approved")

    def test_ceo_approve_overtime_application(self):
        self.assertEquals(ceo_approve_overtime_application(self.overtime_application_id).ceo_approval, "Approved")
