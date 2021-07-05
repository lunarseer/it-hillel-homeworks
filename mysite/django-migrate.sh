#!/bin/bash
python $PWD/manage.py makemigrations
python $PWD/manage.py migrate