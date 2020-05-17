from django.test import TestCase, Client
from django.contrib.auth.models import User

from ...models import Post

class CreatePostViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(CreatePostViewTestCase, cls).setUpClass()
        cls.user = User.objects.create_user(username='testuser', password='testuser')
        cls.superuser = User.objects.create_superuser(username='superuser', password='superuser')

    @classmethod
    def tearDownClass(cls):
        super(CreatePostViewTestCase, cls).tearDownClass()
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
            'title': 'Post title',
            'content': 'Post content .......',
        }


    def test_get_no_auth(self):
        response = self.client.get('/staff/create_post')
        self.assertEqual(404, response.status_code)

    def test_get_with_user_auth(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/staff/create_post')
        self.assertEqual(404, response.status_code)

    def test_get_with_superuser_auth(self):
        self.client.login(username='superuser', password='superuser')
        response = self.client.get('/staff/create_post')
        self.assertEqual(200, response.status_code)

    def test_post_no_auth(self):
        response = self.client.post('/staff/create_post', self.payload)
        self.assertEqual(404, response.status_code)

    def test_post_with_user_auth(self):
        self.client.login(username='testuser', password='testuser')
        response = self.client.post('/staff/create_post', self.payload)
        self.assertEqual(404, response.status_code)

    def test_post_with_superuser_auth(self):
        self.client.login(username='superuser', password='superuser')
        response = self.client.post('/staff/create_post', self.payload)
        self.assertRedirects(response, '/')
        post = Post.objects.get(title=self.payload['title'])
        self.assertEqual(self.payload['title'], post.title)
        self.assertEqual(self.payload['content'], post.content)
