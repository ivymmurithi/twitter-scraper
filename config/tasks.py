from celery import shared_task

from web_scraper_app.views import get_tweets

@shared_task(name = "send_email_task")
def send_email_task():
    return get_tweets()   