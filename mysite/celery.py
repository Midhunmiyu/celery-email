from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

app = Celery('mysite')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')


#celery beat settings

app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request : {self.request!r}')

@app.task
def add(x,y):
    sleep(20)
    return x + y