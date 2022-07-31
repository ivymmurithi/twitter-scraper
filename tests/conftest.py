import pytest
from web_scraper_app.models import Tweets

@pytest.fixture()
def tweet_sample(db):
    tweet = Tweets.objects.create(
        username_id = '12345678910',
        text = 'This is my first tweet',
        tweet_by = 'ivymmurithi',
        retweet_count = 20,
        favorite_count = 100
    )
    return [
        tweet.username_id,
        tweet.text,
        ]