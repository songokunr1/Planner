from flask import Flask, render_template, url_for, request, jsonify
import json
import time
from flask_wtf import CsrfProtect
# from user import login
from flask_sqlalchemy import SQLAlchemy


def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.secret_key = 'hard_to_break'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push() # this does the binding
    return app
db = SQLAlchemy()
app = create_test_app()

from app import routes