#! /bin/sh


rm -r logging.log dev_database.db media/* static/* dev_send_mail/* Feed_RSS/__pycache__/ Feed_RSS/migrations/__pycache__/ Posts/__pycache__/ Posts/migrations/__pycache__/ Posts/migrations/0001_initial.py Posts/service/__pycache__/ Site/__pycache__/ Users/__pycache__/ Users/migrations/__pycache__/ Users/templatetags/__pycache__/


python manage.py makemigrations


python manage.py migrate


python manage.py loaddata fixtures/initial_data.json


python manage.py collectstatic


python manage.py runserver 8080