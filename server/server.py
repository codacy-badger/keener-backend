"""Contain the main server code."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/')
def hello_world():
    """Placeholds route for root."""
    return "Hello, world!"
