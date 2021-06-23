import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Site.settings")

app = Celery("Site")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_check_post": {
        "task": "Posts.tasks.send_check_post",
        "schedule": crontab(minute="*/1"),
    }
}
