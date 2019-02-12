# :bulb: Keener

[![Build Status](https://travis-ci.com/rmcreyes/keener-backend.svg?branch=master)](https://travis-ci.com/rmcreyes/keener-backend)

The backend of an application that lets helps students make the most out of their study groups.

## Setup

To set up the development environment, install [pipenv](https://pipenv.readthedocs.io/en/latest/) to manage dependencies:

```bash
$ pip install pipenv
$ pipenv install --dev
```

The styling tools `pycodestyle` and `pydocstyle` are used to enforce PEP8 coding standards. They are ran upon each Travis build along with `pytest`:

```bash
# you can run commands with the projects dependencies by calling `pipenv run` like:
$ pipenv run pycodestyle .
$ pipenv run pydocstyle .
$ pipenv run pytest .

# alternatively, you can enter the subshell to run the commands without callling `pipenv run`:
$ pipenv shell
$ pycodestyle .
$ pydocstyle .
$ pytest .
```

This project currently uses PostgreSQL for a database. It is being designed to be able to easily switch databases, but until then it is required to
run PostgreSQL for local testing:

```bash
$ sudo apt-get install postgresql
$ sudo service postgresql start
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

The Flask app assumes that there exists a file `.env` in the root directory that contains the credentials to the PostgreSQL database.
It should be set up like so:

```bash
PSQL_USER=USERNAME
PSQL_PW=PASSWORD
PSQL_DB=DBNAME
PSQL_HOST=HOSTNAME
PSQL_PORT=PORTNUM
```

## Scripts

These scripts can help ease the development process:
Running the following script can run the same check the Travis build runs through on each pull request:

```bash
$ ./scripts/travis_build.sh
```

- runs through the same checks the Travis build goes through

```bash
$ ./scripts/postgres_migrate.sh
```

- performs the migration of tables to the PostgreSQL database. Uncomment the first line the first time you have to run it.
