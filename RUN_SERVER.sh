#!/bin/bash

export DJANGO_SUPERUSER_PASSWORD=admin

pip install -r requirements.txt
python $PWD/mysite/manage.py makemigrations
python $PWD/mysite/manage.py migrate
python $PWD/mysite/manage.py createsuperuser --noinput --user admin --email mail@mail.com
python $PWD/mysite/manage.py runserver