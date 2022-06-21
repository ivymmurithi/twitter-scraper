import os
import tweepy

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from .models import Tweets, Usernames


auth = tweepy.OAuthHandler(
    os.environ.get('API_Key'),
    os.environ.get('API_Key_Secret')
)
auth.set_access_token(
    os.environ.get('Access_Token'), 
    os.environ.get('Access_Token_Secret')
)
api = tweepy.API(auth)


def send_email(request):
    latest_tweets = api.user_timeline(user_id='1917319850', count = 1)[0]
    last_tweet_in_db = Tweets.objects.first()
    if latest_tweets.id != int(last_tweet_in_db.username_id):
        current_user = request.user
        subject = 'New tweet!'
        message = 'A new tweet has been posted by {user}'.format(user=current_user)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [current_user.email]
        send_mail(subject,message,email_from,recipient_list)
        print('Sent Successfully')
    else:
        print('Email Failed to Send')
    return HttpResponseRedirect(reverse('get_tweets'))