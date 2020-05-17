from django.test import TestCase
from django.contrib.auth.models import User

from ...forms import ChangePasswordForm


class ChangePasswordFormTestCase(TestCase):
    user = None

    @classmethod
    def setUpClass(cls):
        super(ChangePasswordFormTestCase, cls).setUpClass()
        cls.user = User.objects.create_user(username='testuser', password='testuser')

    @classmethod
    def tearDownClass(cls):
        super(ChangePasswordFormTestCase, cls).tearDownClass()
        try:
            user = User.objects.get(username='testuser')
            user.delete()
        # pylint: disable=bare-except
        except:
            pass

    def test_wrong_old_password(self):
        payload = {
            'old_password': 'thisInNotTheCorrectPassword',
            'new_password': 'passwd1',
            'new_password_repeat': 'passwd1',
        }
        form = ChangePasswordForm(self.user, data=payload)
        self.assertFalse(form.is_valid())
        self.assertIn('Podane stare hasło jest błędne', form.errors['__all__'])

    def test_password_differ(self):
        payload = {
            'old_password': 'testuser',
            'new_password': 'passwd1',
            'new_password_repeat': 'passwd2',
        }
        form = ChangePasswordForm(self.user, data=payload)
        self.assertFalse(form.is_valid())
        self.assertIn('Hasła się różnią', form.errors['__all__'])

    def test_password_are_equal(self):
        payload = {
            'old_password': 'testuser',
            'new_password': 'testuser',
            'new_password_repeat': 'testuser',
        }
        form = ChangePasswordForm(self.user, data=payload)
        self.assertFalse(form.is_valid())
        self.assertIn('Nowe hasło jest takie samo jak stare', form.errors['__all__'])

    def test_no_errors(self):
        payload = {
            'old_password': 'testuser',
            'new_password': 'testuser1',
            'new_password_repeat': 'testuser1',
        }
        form = ChangePasswordForm(self.user, data=payload)
        self.assertTrue(form.is_valid())
