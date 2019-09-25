from django.test import TestCase
from django.urls import resolve, reverse
from django.utils import timezone

from employees.models import Employee
from overtime.models import OvertimeApplication
from role.views.cfo_views import cfo_overtime_page, cfo_approve_overtime
from role.views.hod_views import hod_role_page, hod_reject_overtime, hod_amend_overtime_page
from settings.models import Currency


class TestUrl(TestCase):

    def check_page_url_is_resolved(self, url_name, view_function_name, args=None):
        url = reverse(url_name, args=args)
        self.assertEquals(resolve(url).func, view_function_name)

    # CFO page urls  test
    def test_cfo_overtime_page_is_resolved(self):
        self.check_page_url_is_resolved('cfo_overtime_page', cfo_overtime_page)

    # HOD page urls test
    def test_hod_role_page_is_resolved(self):
        self.check_page_url_is_resolved('hod_role_page', hod_role_page)

    def test_hod_amend_overtime_page_is_resolved(self):
        self.check_page_url_is_resolved('hod_amend_overtime_page', hod_amend_overtime_page, args=[1])

    #     Processes test
    # HOD reject overtime application
    def test_hod_reject_overtime_is_resolved(self):
        url = reverse('hod_reject_overtime', args=[1])
        self.assertEquals(resolve(url).func, hod_reject_overtime)

    def test_cfo_approve_overtime_is_resolved(self):
        self.check_page_url_is_resolved('cfo_approve_overtime',cfo_approve_overtime,args=[1])