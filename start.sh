#!/bin/bash

clear
source .venv/bin/activate

python ./RavaDev/ manage.py makemigrations


python ./RavaDev/manage.py migrate


clear


nohup python ./RavaDev/manage.py runserver 0.0.0.0:8001 > output.log 2>&1 &


