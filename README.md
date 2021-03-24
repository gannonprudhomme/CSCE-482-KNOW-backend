# Team KNOW Backend

## Install

0. Clone the repository - `git clone https://github.com/gannonprudhomme/CSCE-482-KNOW-Backend.git/`

1. Install Python 3.7 from [here](https://www.python.org/downloads/)

2. `pip install --user pipenv`

3. `pipenv install --dev`

4. `pipenv shell`

5. `python know/manage.py runserver`

6. You can now navigate to localhost:8000/ and see the server running!

## Setup

We'll be using pylint to lint the project.

## Running linting

1. `cd know/`

2. `pipenv run lint`

## Run tests

1. `cd know/`

2. `pipenv run test` or `pytest`

## Setup pylint in VSCode

I have instructions from a previous project (that has an identical tech stack) for setting up pylint to automatically lint in VSCode [here](https://github.com/aggie-coding-club/Rev-Registration/wiki/Setup-Pylint).

## Troubleshooting

### Pipenv is not found

You probably don't have the Python scripts folder in your PATH
