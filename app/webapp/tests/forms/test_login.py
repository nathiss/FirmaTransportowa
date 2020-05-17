from django.test import TestCase

from ...forms import LoginForm

class LoginFormTestCase(TestCase):
    def test_no_login(self):
        data = {
            'passwd': '123',
            'remember_me': True,
        }
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

    def test_no_passwd(self):
        data = {
            'login': '123',
            'remember_me': True,
        }
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

    def test_no_remember_me(self):
        data = {
            'login': '123',
            'passwd': '123',
        }
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_login(self):
        data = {
            'login': '',
            'passwd': '123',
            'remember_me': True,
        }
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

    def test_empty_passwd(self):
        data = {
            'login': '123',
            'passwd': '',
            'remember_me': True,
        }
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())
