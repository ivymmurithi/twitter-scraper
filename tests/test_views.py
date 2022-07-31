import unittest
from django.contrib.auth.models import User
from django.test import Client, TestCase

class ViewTestCase(unittest.TestCase):
    client = Client()

    def test_home_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)

    def test_register_url(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_liked_url(self):
        response = self.client.get('/like/{tweet_clicked_id}/')
        self.assertEqual(response.status_code, 404)

    def test_detailed_view(self):
        response = self.client.get('/detailed_view/{tweet_clicked_id}/')
        self.assertEqual(response.status_code, 404)

    def test_logout_user(self):
        response = self.client.get('/logoutuser/')
        self.assertEqual(response.status_code, 404)

class LoginTest(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)