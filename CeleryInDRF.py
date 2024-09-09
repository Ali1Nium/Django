#1) Making a new file with name celery.py (in default app )
#adding this cod to celery.py

import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'First_Project.settings')

app = Celery('First_Project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

##
# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


#2)Importing app name to __init__.py 


from .celery import app as celery_app

__all__ = ["celery_app"]


#3) Adding setting to setting file :

# Celery Configuration Options
CELERY_TIMEZONE = "Asia/Tehran"
# CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60


#4)Making a simple tasks.py in evry app that we need :

from celery import shared_task 

from Mashin_Learning.models import Students

from django.db.models import Sum 



@shared_task()
def sample_test():
    pass

@shared_task()

def get_test_test():
    student = Students.objects.all()


    print(f"name : {student}")