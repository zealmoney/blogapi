from django.test import TestCase

from django.contrib.auth import get_user_model

from .models import Post

class TestBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        cls.user = get_user_model().objects.create(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'secret'
        )

        cls.posts = Post.objects.create(
            title = 'A good title',
            body = 'A nice body content',
            author = cls.user
        )
        
    def test_post_model(self):
        self.assertEqual(self.posts.author.username, 'testuser')
        self.assertEqual(self.posts.title, 'A good title')
        self.assertEqual(self.posts.body, 'A nice body content')
        self.assertEqual(str(self.posts), 'A good title')
