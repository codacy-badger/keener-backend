"""Contain the main server code."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from environs import Env

env = Env()
env.read_env()
is_testing = env.bool("TESTING")

app = Flask(__name__)
POSTGRES = {
    'user': env.str('PSQL_USER'),
    'pw': env.str('PSQL_PW'),
    'db': env.str('PSQL_DB'),
    'host': env.str('PSQL_HOST'),
    'port': env.str('PSQL_PORT')
}
psql_uri = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_DATABASE_URI'] = psql_uri
db = SQLAlchemy()
db.init_app(app)


@app.route('/')
def hello_world():
    """Placeholds route for root."""
    return "Hello, world!"


if __name__ == '__main__':
    app.run()
