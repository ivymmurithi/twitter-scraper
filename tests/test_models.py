from django.test import TestCase

from web_scraper_app.models import Tweets, Usernames


class TweetsTestClass(TestCase):

    # First, prepare any state you will need to perform the action you want to try
    def setUp(self):
        self.tweet1 = Tweets.objects.create(
            username_id='1234567899', 
            text='This is my first tweet!'
        )

    # Then perform that action.

    # Finally, verify the consequences of the action are those that you expected.
    def test_tweet_instance(self):
        self.assertTrue(isinstance(self.tweet1, Tweets))

    def test_filter_method(self):
        assert Tweets.objects.filter(
            username_id__icontains=self.tweet1.username_id
        )

    def test_create_method(self):
        tweet = Tweets.objects.create(
            username_id = '12345678910',
            text = 'This is my first tweet',
            tweet_by = 'ivymmurithi',
            retweet_count = 20,
            favorite_count = 100
        )
        assert Tweets.objects.filter(
            username_id = '12345678910',
            text = 'This is my first tweet',
            tweet_by = 'ivymmurithi',
            retweet_count = 20,
            favorite_count = 100
        ).exists()

    def test_field_access(tweet_sample):
        assert tweet_sample
        

class UsernamesTestClass(TestCase):

    def setUp(self):
        self.username1 = Usernames(name='ivy', username='ivymmurithi')
        self.username1.save()

    def test_usernames_instance(self):
        self.assertTrue(isinstance(self.username1, Usernames))