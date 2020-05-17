from django.test import TestCase, Client
from django.contrib.auth.models import User


class RegisterViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(RegisterViewTestCase, cls).setUpClass()
        User.objects.create_user(username='testuser', password='testuser')

    @classmethod
    def tearDownClass(cls):
        super(RegisterViewTestCase, cls).tearDownClass()
        try:
            user = User.objects.get(username='testuser')
            user.delete()
        # pylint: disable=bare-except
        except:
            pass

    def setUp(self):
        self.client = Client()

    def test_get_with_auth(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/register/')
        self.assertRedirects(response, '/')

    def test_get_no_auth(self):
        response = self.client.get('/register/')
        self.assertEqual(200, response.status_code)

    def test_post_new_user(self):
        payload = {
            'login': 'newuser',
            'passwd': 'newuser',
            'repeatPasswd': 'newuser',
            'email': 'newuser@example.com',
            'first_name': 'Asd',
            'last_name': 'Gbd',
            'phone_number': '5' * 9,
            'pesel': '1' * 11,
        }
        response = self.client.post('/register/', payload)
        self.assertRedirects(response, '/')

    def test_post_existing_user(self):
        payload = {
            'login': 'testuser',
            'passwd': 'testuser',
            'repeatPasswd': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Asd',
            'last_name': 'Gbd',
            'phone_number': '5' * 9,
            'pesel': '1' * 11,
        }
        self.assertRaises(Exception, lambda: self.client.post('/register/', payload))
