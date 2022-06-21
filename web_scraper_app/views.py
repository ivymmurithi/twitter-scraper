# Third party Libraries
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse

# Django apps
from .forms import RegisterForm
from .models import Tweets, Usernames
from config import settings

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        return redirect('/login/', {'register_form':register_form})
    else:
        register_form = RegisterForm()
    return render (
        request,'registration/register.html',{'register_form':register_form}
    )


@login_required
def get_tweets(request):

    usernames = settings.client.get_users(usernames=['ivymmurithi'], user_auth=True)    
    for user in usernames.data:
        name = user.name
        username = user.username
        if Usernames.objects.filter(
            name__icontains=name,username__icontains=username).exists() is False:
            Usernames.objects.create(name=name, username=username)
            print('User saved successfully')
        else:
            print('User already exists')


    user_tweets = settings.api.user_timeline(screen_name='ivymmurithi')
    for user_tweet in user_tweets:
        username_id = user_tweet.id
        text = user_tweet.text
        tweet_by = user_tweet.user.screen_name
        retweet_count = user_tweet.retweet_count
        favorite_count = user_tweet.favorite_count

        if Tweets.objects.filter(
            username_id__icontains=username_id,text__icontains=text).exists() is False:
            Tweets.objects.create(
                username_id=username_id, 
                text=text, 
                tweet_by=tweet_by,
                retweet_count=retweet_count,
                favorite_count=favorite_count
            )
            print('Tweets saved successfully')

        else:
            print('Tweets already exists')

    retrieved_tweets = Tweets.objects.all()
    retrieved_users = Usernames.objects.all()

    return render(
        request, 'index.html', {'tweets':retrieved_tweets, 'users':retrieved_users}
    )

@login_required
def detailed_view(request, tweet_clicked_id):
    tweets_in_db = Tweets.objects.filter(pk=tweet_clicked_id)
    retrieved_users = Usernames.objects.all()
    return render(
        request, 'detailed_view.html', {'tweets_in_db':tweets_in_db, 'users':retrieved_users}
    )

@login_required
def like_tweet(request, tweet_clicked_id):
    if request.method == 'POST':
        settings.client.like(tweet_clicked_id, user_auth=True)
        print('Tweet liked successfully')
    else:
        print('Tweet not liked')
    return HttpResponseRedirect(reverse('get_tweets')) 

def logoutuser(request):
    logout(request)
    return redirect('login')