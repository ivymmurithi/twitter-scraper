from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('', include('django.contrib.auth.urls')),
    path('home/', views.display_tweets, name='display_tweets'),
    path('logoutuser',views.logoutuser, name='logoutuser'),
    path('like/<int:tweet_clicked_id>/', views.like_tweet, name='like'),
    path('detailed_view/<int:tweet_clicked_id>/', views.detailed_view, name='detailed_view'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)