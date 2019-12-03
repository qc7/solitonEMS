from django.test import TestCase,Client

from check_methods_for_tests import check_response_200_ok, check_template_and_status_code
from payroll.views import payroll_page


class TestPayrollView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_payroll_page_view_get(self):
        check_template_and_status_code(self, payroll_page, "payroll/payroll_page.html")

    def test_manage_payroll_records_page_renders(self):
        check_template_and_status_code(self, payroll_page, "payroll/payroll_page.html")
