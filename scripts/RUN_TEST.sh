#!/bin/bash
pip install -r ../requirements.txt
export DJANGO_SUPERUSER_PASSWORD=admin
python ../mysite/manage.py createsuperuser --noinput --user admin --email mail@mail.com
python ../mysite/manage.py makemigrations
python ../mysite/manage.py migrate