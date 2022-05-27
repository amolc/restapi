#!/bin/bash
source env/bin/activate
pip install -r requirements.txt
cd restserver
python manage.py runserver 0.0.0.0:7000
