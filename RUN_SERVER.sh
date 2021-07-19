#!/bin/bash
pip install -r $PWD/requirements.txt

source CONSTANTS.sh

flake8

export DJANGO_SUPERUSER_PASSWORD=admin

python $PWD/mysite/manage.py makemigrations
python $PWD/mysite/manage.py migrate

python $PWD/mysite/manage.py createsuperuser --noinput --user admin --email mail@mail.com

python $PWD/mysite/manage.py generate_teachers 50
python $PWD/mysite/manage.py generate_students 100

python $PWD/mysite/manage.py runserver