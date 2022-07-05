from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='register'),
    path('', include('django.contrib.auth.urls')),
    path('home/', views.get_tweets, name='get_tweets'),
    path('logoutuser',views.logoutuser, name='logoutuser'),
    path('like/<int:tweet_clicked_id>/', views.like_tweet, name='like'),
    path('detailed_view/<int:tweet_clicked_id>/', views.detailed_view, name='detailed_view'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)