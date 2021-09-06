from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #User
        test_user = User.objects.create(username='test', password='test')
        test_user.save()

        #Post
        test_post = Post.objects.create(author=test_user, title='Post Title', body='Post Body')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'test')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(body, 'Post Body')