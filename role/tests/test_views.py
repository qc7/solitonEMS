from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from employees.models import Employee
from overtime.models import OvertimeApplication
from role.tests.check_functions import check_template_and_status_code, check_process_view_get
from settings.models import Currency


class TestRoleView(TestCase):

    def setUp(self):
        self.client = Client()

        currency = Currency.objects.create(
            code="UGX"
        )

        self.supervisee = Employee.objects.create(
            first_name="Test",
            last_name="Employee",
            start_date=timezone.now().today(),
            dob=timezone.now().today(),
            currency=currency
        )
        self.supervisor = Employee.objects.create(
            first_name="Test",
            last_name="Supervisor",
            start_date=timezone.now().today(),
            dob=timezone.now().today(),
            currency=currency
        )
        self.overtime_application = OvertimeApplication.objects.create(
            status="Pending",
            date=timezone.now().today(),
            start_time=timezone.now().time(),
            end_time=timezone.now().time(),
            description="Testing overtime application",
            supervisee=self.supervisee,
            supervisor=self.supervisor
        )

    # CFO ROLE TEST
    def test_cfo_overtime_page_view_get(self):
        check_template_and_status_code(self, 'cfo_overtime_page', "role/cfo/overtime.html")

    def test_cfo_amend_overtime_page_view_get(self):
        check_template_and_status_code(self, 'cfo_amend_overtime_page', 'role/cfo/amend_overtime.html',
                                       args=[self.overtime_application.id])

    # Process
    def test_cfo_reject_overtime_view_get(self):
        check_process_view_get(self, 'cfo_reject_overtime', args=[self.overtime_application.id])

    def test_cfo_approve_overtime_view_get(self):
        check_process_view_get(self, 'cfo_approve_overtime', args=[self.overtime_application.id])

    def test_cfo_amend_overtime(self):
        check_process_view_get(self, 'cfo_amend_overtime')

    # HOD ROLE TEST
    def test_hod_role_page_view_get(self):
        check_template_and_status_code(self, 'hod_role_page', 'role/hod/dashboard.html')

    def test_hod_overtime_page_view_get(self):
        check_template_and_status_code(self, 'hod_overtime_page', 'role/hod/overtime.html')

    def test_hod_amend_overtime_page_view_get(self):
        check_template_and_status_code(self, 'hod_amend_overtime_page', 'role/hod/amend_overtime.html',
                                       args=[self.overtime_application.id])

    # HOD PROCESS TESTS
    def test_hod_reject_overtime_view_get(self):
        check_process_view_get(self, 'hod_reject_overtime', args=[self.overtime_application.id])

    def test_hod_approve_overtime_view_get(self):
        check_process_view_get(self, 'hod_approve_overtime', args=[self.overtime_application.id])

    def test_hod_amend_overtime_post(self):
        response = self.client.post(reverse('hod_amend_overtime'), {
            'id': self.overtime_application.id,
            'status': "Approved",
            'date': '2019-09-17',
            'start_time': timezone.now().time(),
            'end_time': timezone.now().time(),
            'description': 'Testing overtime application',
            'supervisee': self.supervisee,
            'supervisor': self.supervisor
        })

        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response)

    # CEO ROLE TEST
    def test_ceo_reject_overtime_view_get(self):
        check_process_view_get(self, 'ceo_reject_overtime', args=[self.overtime_application.id])

    def test_ceo_approve_overtime_view_get(self):
        check_process_view_get(self, 'ceo_approve_overtime', args=[self.overtime_application.id])

    def test_ceo_amend_overtime_page_view_get(self):
        check_template_and_status_code(self, 'ceo_amend_overtime_page', 'role/ceo/amend_overtime.html',
                                       args=[self.overtime_application.id])
