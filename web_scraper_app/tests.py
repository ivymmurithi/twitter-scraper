from django.test import TestCase

from .models import Tweets, Usernames


class TweetsTestClass(TestCase):

    def setUp(self):
        self.tweet1 = Tweets.objects.create(
            username_id='1234567899', text='This is my first tweet!'
        )

    def test_tweet_instance(self):
        self.assertTrue(isinstance(self.tweet1, Tweets))


class UsernamesTestClass(TestCase):

    def setUp(self):
        self.username1 = Usernames(name='ivy', username='ivymmurithi')
        self.username1.save()

    def test_usernames_instance(self):
        self.assertTrue(isinstance(self.username1, Usernames))

