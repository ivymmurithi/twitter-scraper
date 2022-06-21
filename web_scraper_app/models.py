from django.db import models
from django.contrib.auth.models import User

class Tweets(models.Model):
    username_id = models.CharField(null=True, max_length=100)
    text = models.TextField(null=True)
    tweet_by = models.CharField(null=True, max_length=100)
    retweet_count = models.IntegerField(null=True)
    favorite_count = models.IntegerField(null=True)

    def __str__(self):
        return self.tweet_by


class Usernames(models.Model):
    name = models.CharField(null=True, max_length=100)
    username = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user