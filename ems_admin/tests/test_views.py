from django.test import TestCase, Client
from django.urls import reverse

from check_methods_for_tests import check_response_200_ok
from ems_admin.views import manage_users_page, view_users_page


class TestAdminView(TestCase):
    def setUp(self):
        pass

    def test_manage_users_page_renders(self):
        response = self.client.get(reverse(manage_users_page))
        check_response_200_ok(self, response, 'ems_admin/manage_users.html')

    def test_view_users_page_renders(self):
        response = self.client.get(reverse(view_users_page))
        check_response_200_ok(self, response, 'ems_admin/view_users.html')

