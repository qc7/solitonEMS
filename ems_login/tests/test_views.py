from django.contrib.auth.models import User
from django.test import TestCase, Client

from ems_login.tests.check_methods import check_process_view_post, check_template_and_status_code
from ems_login.views import login_view,login_page,logout_view


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user_username = "test_user"
        self.test_user_password = 'secret'
        User.objects.create_user(username=self.test_user_username, password=self.test_user_password)

    # Test whether view returns the right status code and template
    def test_login_view_user_not_authenticated(self):
        check_template_and_status_code(self, login_view, "ems_login/login.html")

    def test_login_view_user_is_authenticated(self):
        check_process_view_post(self, login_view, {'username': self.test_user_username, 'password': self.test_user_password})

    def test_login_page_view_get(self):
        check_template_and_status_code(self,login_page,"ems_login/login.html")

    def test_logout_process_view_get(self):
        check_template_and_status_code(self, logout_view,"ems_login/login.html")



