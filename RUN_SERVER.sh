#!/bin/bash
#source $PWD/venv/bin/activate
pip install -r requirements.txt
python $PWD/mysite/manage.py makemigrations
python $PWD/mysite/manage.py migrate