from django.test import TestCase, Client
from django.contrib.auth.models import User

class ChangePasswordViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='testuser', password='testuser')

    def tearDown(self):
        try:
            user = User.objects.get(username='testuser')
            user.delete()
        # pylint: disable=bare-except
        except:
            pass

    def test_get_request_no_auth(self):
        response = self.client.get(r'/user/change_password')
        self.assertRedirects(response, r'/')

    def test_post_request_no_auth(self):
        response = self.client.post(r'/user/change_password')
        self.assertRedirects(response, r'/')

    def test_get_request_with_auth(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.get(r'/user/change_password')
        self.assertEqual(200, response.status_code)

    def test_post_request_with_auth(self):
        self.client.login(username='testuser', password='testuser')
        payload = {
            'old_password': 'testuser',
            'new_password': 'passwd1',
            'new_password_repeat': 'passwd1'
        }
        response = self.client.post(r'/user/change_password', payload)
        self.assertEqual(302, response.status_code)
