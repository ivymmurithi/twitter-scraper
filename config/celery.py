import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
# Using namespace='CELERY' tells Celery to only read configurations that are uppercase and start with the `CELERY_` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "scrape-tweets-every-5-minutes": {
        'task' : 'send_email_task',
        'schedule' : 300 
    }
}

app.autodiscover_tasks()