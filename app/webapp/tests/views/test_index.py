from django.test import TestCase, Client

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_get_no_articles(self):
        response = self.client.get('/')
        self.assertContains(response, 'Tabela aktualności w bazie danych jest pusta.')

    def test_post(self):
        response = self.client.post('/', {})
        self.assertEqual(405, response.status_code)
