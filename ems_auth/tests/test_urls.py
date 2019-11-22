from django.contrib.auth.views import PasswordResetView
from django.test import TestCase
from django.urls import reverse, resolve

from ems_auth.tests.check_methods import check_page_url_is_resolved
from ems_auth.views import login_view, login_page, logout_view


class TestUrls(TestCase):

    def test_login_url_is_resolved(self):
        check_page_url_is_resolved(self, "login", login_view)

    def test_login_page_url_is_resolved(self):
        check_page_url_is_resolved(self, "loginAccounts", login_page)

    def test_logout_url_is_resolved(self):
        check_page_url_is_resolved(self, "logout", logout_view)


