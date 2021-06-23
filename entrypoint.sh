#! /bin/sh


sleep 5


rm -r logging.log celerybeat-schedule static/* media/* Posts/migrations/0001_initial.py


python3 manage.py makemigrations


python3 manage.py migrate


python3 manage.py loaddata fixtures/initial_data.json


python3 manage.py collectstatic


celery -A Site worker -l info & celery -A Site beat -l info & gunicorn Site.wsgi:application -b 0.0.0.0:8000 --reload
