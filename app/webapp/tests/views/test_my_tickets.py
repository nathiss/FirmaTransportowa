from django.test import TestCase, Client
from django.contrib.auth.models import User

from ...models import Client as ClientModel

class TicketsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TicketsViewTestCase, cls).setUpClass()
        cls.user = User.objects.create_user(username='testuser', password='testuser')

    @classmethod
    def tearDownClass(cls):
        super(TicketsViewTestCase, cls).tearDownClass()
        try:
            user = User.objects.get(username='testuser')
            user.delete()
        # pylint: disable=bare-except
        except:
            pass

    @classmethod
    def get_client(cls):
        c = ClientModel()
        c.user = cls.user
        c.first_name = 'Abc'
        c.last_name = 'Asdf'
        c.email = 'abs@examle.com'
        c.phone_number = '1' * 9
        c.pesel = '1' * 11
        return c

    def setUp(self):
        self.client = Client()

    def tearDown(self):
        for client in ClientModel.objects.all():
            client.delete()


    def test_get_no_auth(self):
        response = self.client.get('/user/tickets')
        self.assertRedirects(response, '/')

    def test_get_with_auth_no_client(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/user/tickets')
        self.assertEqual(404, response.status_code)

    def test_get_with_auth_and_client(self):
        client_model = TicketsViewTestCase.get_client()
        client_model.save()
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/user/tickets')
        self.assertEqual(200, response.status_code)

    def test_get_with_auth_no_tickets(self):
        client_model = TicketsViewTestCase.get_client()
        client_model.save()
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/user/tickets')
        self.assertContains(response, 'Nie masz żadnych biletów')

    def test_post(self):
        response = self.client.post('/user/tickets')
        self.assertEqual(405, response.status_code)
