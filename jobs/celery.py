import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")

import django
django.setup()

app = Celery("todo_list")
app.config_from_object("django.conf:settings", namespace="CELERY")

import jobs.tasks