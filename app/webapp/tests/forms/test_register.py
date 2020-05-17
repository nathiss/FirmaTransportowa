from django.test import TestCase

from ...forms import RegisterForm

class RegisterFormTestCase(TestCase):
    def setUp(self):
        self.data = {
            'login': 'tesetuser',
            'passwd': 'testuser',
            'repeatPasswd': 'testuser',
            'email': 'abc@example.com',
            'first_name': 'Asd',
            'last_name': 'Gbd',
            'phone_number': '5' * 9,
            'pesel': '1' * 11,
        }

    def test_different_passwords(self):
        self.data['repeatPasswd'] = '123'
        form = RegisterForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_phone_number_with_letters(self):
        self.data['phone_number'] = '1234gh789'
        form = RegisterForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_pesel_with_letters(self):
        self.data['phone_number'] = '1234gh78912'
        form = RegisterForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_good(self):
        form = RegisterForm(data=self.data)
        self.assertTrue(form.is_valid())
