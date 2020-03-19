from django.test import TestCase

from .models import Post
from django.contrib.auth.models import User
from users.forms import *   # import all forms


class BlogModelTest(TestCase):

    def test_string(self):
        usr = User.objects.create(username='myuser')
        post = Post(title='This new test', content='this is a new  test blog', author=usr)
        self.assertEqual(str(post), 'This new test')

class Setup_Class(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserRegistrationForm(data={'email': "user@mp.com", 'password1': "Purva290790", 'password2': "Purva290790", 'username': "user"})
        self.assertTrue(form.is_valid())