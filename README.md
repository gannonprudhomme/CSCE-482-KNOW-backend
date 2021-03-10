# Team KNOW Backend

## Install

0. Clone the repository - `git clone https://github.com/gannonprudhomme/CSCE-482-KNOW-Backend.git/`

1. Install Python 3.7 from [here](https://www.python.org/downloads/)

2. `pip install --user pipenv`

3. `pipenv install`

4. `python manage.py know/runserver`

5. You can now navigate to localhost:8000/ and see the server running!

## Setup

We'll be using pylint to lint the project.

## Running linting

1. `cd know/`

2. `pipenv run lint`

## Run tests

1. `cd know/`

2. `pipenv run test` or `pytest`

## Troubleshooting

### Pipenv is not found

You probably don't have the Python scripts folder in your PATH
