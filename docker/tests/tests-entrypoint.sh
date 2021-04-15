#!/bin/sh
export DJANGO_SETTINGS_MODULE=know.settings
cd know/ # Must be in the first know/ directory to run the tests
pipenv run test
