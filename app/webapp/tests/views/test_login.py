from django.test import TestCase, Client
from django.contrib.auth.models import User

class LoginViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(LoginViewTestCase, cls).setUpClass()
        User.objects.create_user(username='testuser', password='testuser')

    @classmethod
    def tearDownClass(cls):
        super(LoginViewTestCase, cls).tearDownClass()
        try:
            user = User.objects.get(username='testuser')
            user.delete()
        # pylint: disable=bare-except
        except:
            pass

    def setUp(self):
        self.client = Client()


    def test_get_no_auth(self):
        response = self.client.get('/login/')
        self.assertEqual(200, response.status_code)

    def test_get_with_auth(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/login/')
        self.assertRedirects(response, '/')

    def test_post_with_wrong_credentials(self):
        payload = {
            'login': 'notAUser',
            'passwd': '123',
            'remembe_me': False,
        }
        response = self.client.post('/login/', data=payload)
        self.assertEqual(200, response.status_code)

    def test_post_with_correct_credentials(self):
        payload = {
            'login': 'testuser',
            'passwd': 'testuser',
            'remember_me': False,
        }
        response = self.client.post('/login/', data=payload)
        self.assertRedirects(response, '/')

    def test_post_with_remember_me_false(self):
        payload = {
            'login': 'testuser',
            'passwd': 'testuser',
            'remember_me': False,
        }
        self.client.post('/login/', data=payload)
        self.assertEqual(3600, self.client.session.get_expiry_age())

    def test_post_with_remember_me_true(self):
        payload = {
            'login': 'testuser',
            'passwd': 'testuser',
            'remember_me': True,
        }
        self.client.post('/login/', data=payload)
        self.assertEqual(7776000, self.client.session.get_expiry_age())
