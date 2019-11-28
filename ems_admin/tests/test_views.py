from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from check_methods_for_tests import check_response_200_ok
from ems_admin.models import EMSPermission
from ems_admin.views import manage_users_page, view_users_page, edit_user_page, manage_user_permissions_page, \
    edit_user_permission_page

User = get_user_model()


class TestAdminView(TestCase):
    def setUp(self):
        user = User.objects.create_user(email='something@something.com', password='secret')
        permission = EMSPermission.objects.create(name="testing perm", user=user)

    def test_manage_users_page_renders(self):
        response = self.client.get(reverse(manage_users_page))
        check_response_200_ok(self, response, 'ems_admin/manage_users.html')

    def test_edit_user_page_renders(self):
        response = self.client.get(reverse(edit_user_page, args=[1]))
        check_response_200_ok(self, response, 'ems_admin/edit_user.html')

    def test_manage_user_permissions_page_renders(self):
        response = self.client.get(reverse(manage_user_permissions_page, args=[1]))
        check_response_200_ok(self, response, 'ems_admin/manage_user_permissions.html')

    def test_edit_user_permission_page_renders(self):
        response = self.client.get(reverse(edit_user_permission_page, args=[1]))
        check_response_200_ok(self, response, 'ems_admin/edit_user_permission.html')

    def test_view_users_page_renders(self):
        response = self.client.get(reverse(view_users_page))
        check_response_200_ok(self, response, 'ems_admin/view_users.html')
