import unittest

from django.test import Client

class ViewTestCase(unittest.TestCase):
    client = Client()

    def test_home_url(self):
        response = self.client.get('/home/')
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