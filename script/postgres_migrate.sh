/etc/init.d/postgresql start
# pipenv run python manage.py db init
pipenv run python manage.py db migrate
pipenv run python manage.py db upgrade