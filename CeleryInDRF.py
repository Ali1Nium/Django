"""
sudo docker -d -p 5672:5672 rabbitmq 
sudo docker ps
pip install celery 
celery -A {name_of_file} worker -l INFO 
celery -A {name_of_file} worker --concurrency {number} -l INFO 
celery -A {name_of_file} worker --concurrency {number} --soft_time_limit {second}-l INFO 
celery -A {name_of_beat} baet -l INFO
"""

"""
Requirments.text ==> 

amqp==5.2.0
billiard==4.2.0
celery==5.4.0
click==8.1.7
click-didyoumean==0.3.1
click-plugins==1.1.1
click-repl==0.3.0
kombu==5.4.0
prompt_toolkit==3.0.47
python-dateutil==2.9.0.post0
six==1.16.0
tzdata==2024.1
vine==5.1.0
wcwidth==0.2.13

"""

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
