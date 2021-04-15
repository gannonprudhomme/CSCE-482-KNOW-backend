#!/bin/sh
export DJANGO_SETTINGS_MODULE=know.settings
cd know/ 
pipenv run server 0.0.0.0:8000
