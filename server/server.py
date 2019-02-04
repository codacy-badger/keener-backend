"""Contain the main server code."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from environs import Env

env = Env()
env.read_env()
is_testing = env.bool("TESTING")
db_type = env.str("DB_TYPE")
db_uri = env.str("LOCAL_POSTGRESQL_URI")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy()
db.init_app(app)


@app.route('/')
def hello_world():
    """Placeholds route for root."""
    return "Hello, world!"


if __name__ == '__main__':
    app.run()
