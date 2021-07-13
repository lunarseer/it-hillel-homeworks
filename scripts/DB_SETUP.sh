#!/bin/bash
pip install -r ../requirements.txt
export DJANGO_SUPERUSER_PASSWORD=admin
source CONSTANTS.sh
python ../mysite/manage.py createsuperuser --noinput --user admin --email mail@mail.com
python ../mysite/manage.py makemigrations
python ../mysite/manage.py migrate

python ../mysite/manage.py generate_teachers 50
python ../mysite/manage.py generate_students 100