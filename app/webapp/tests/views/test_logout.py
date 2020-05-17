from django.test import TestCase, Client
from django.contrib.auth.models import User

class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_no_auth(self):
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/')

    def test_get_with_auth(self):
        User.objects.create_user(username='testuser', password='testuser')
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/')

    def test_get_logged_in_should_logout(self):
        User.objects.create_user(username='testuser', password='testuser')
        self.client.login(username='testuser', password='testuser')
        self.client.get('/logout/')
        self.assertFalse(self.client.logout())

    def test_post(self):
        response = self.client.post('/', {})
        self.assertEqual(405, response.status_code)
