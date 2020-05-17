from django.test import TestCase, Client
from django.contrib.auth.models import User

from ...models import Place


class CreatePlaceViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CreatePlaceViewTestCase, cls).setUpClass()
        User.objects.create_user(username='testuser', password='testuser')
        User.objects.create_superuser(username='superuser', password='superuser')

    @classmethod
    def tearDownClass(cls):
        super(CreatePlaceViewTestCase, cls).tearDownClass()
        try:
            user = User.objects.get(username='testuser')
            user.delete()
        # pylint: disable=bare-except
        except:
            pass
        try:
            user = User.objects.get(username='superuser')
            user.delete()
        # pylint: disable=bare-except
        except:
            pass

    def setUp(self):
        self.client = Client()
        self.payload = {
            'city': 'Miasto',
            'street': 'Ulica',
            'stop_name': 'Nazwa przystanku',
        }

    def test_get_no_auth(self):
        response = self.client.get('/staff/create_place')
        self.assertEqual(404, response.status_code)

    def test_get_with_user_auth(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/staff/create_place')
        self.assertEqual(404, response.status_code)

    def test_get_with_superuser_auth(self):
        self.client.login(username='superuser', password='superuser')
        response = self.client.get('/staff/create_place')
        self.assertEqual(200, response.status_code)

    def test_post_no_auth(self):
        response = self.client.post('/staff/create_place', self.payload)
        self.assertEqual(404, response.status_code)

    def test_post_with_user_auth(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.post('/staff/create_place', self.payload)
        self.assertEqual(404, response.status_code)

    def test_post_with_superuser_auth(self):
        self.client.login(username='superuser', password='superuser')
        response = self.client.post('/staff/create_place', self.payload)
        self.assertRedirects(response, '/staff/create_place')
        place = Place.objects.get(city=self.payload['city'],
                                  street=self.payload['street'],
                                  stop_name=self.payload['stop_name'])
        self.assertIsNotNone(place)
