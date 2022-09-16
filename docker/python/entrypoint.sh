#!/bin/bash

/VProduction/docker/python/wait-for-it.sh db:3306 -- python /VProduction/manage.py migrate
gunicorn VProduction.wsgi:application --bind 0.0.0.0:8000