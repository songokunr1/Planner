from flask import Flask, render_template, url_for, request
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push() # this does the binding
    return app

def create_production_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push()
    return app


app = create_test_app()
from .app import app