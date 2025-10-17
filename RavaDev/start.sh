#!/bin/bash


git pull
git push


	
clear
source .venv/bin/activate

python manage.py makemigrations


python manage.py migrate


clear


python manage.py runserver 8001

