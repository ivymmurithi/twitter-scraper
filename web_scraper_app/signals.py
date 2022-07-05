import re
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from requests import request

from config import settings
from django.core.mail import send_mail
from .models import Profile,Tweets

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()

@receiver(post_save, sender=Tweets)
def create_tweet(sender, instance, **kwargs):
    if instance:
        tweet = instance.text
        subject = 'New tweet!'
        message = f'A new tweet has been posted {tweet}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['ivymurithi@gmail.com']
        send_mail(subject,message,email_from,recipient_list)
        print('Email Sent Succesfully')
