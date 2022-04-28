from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery("config", include=['core.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#app.conf.beat_schedule = {
    #"status_beat-5-minute": {
        #"task": "core.tasks.status_beat",
        #"schedule" : crontab(minute="*/5")

    #}

#}
