from flask import Flask, render_template, url_for, request, jsonify
import json
from user_model import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash


def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.secret_key = 'hard_to_break'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    # Dynamically bind SQLAlchemy to application
    # db.init_app(app)
    app.app_context().push() # this does the binding
    return app

db = SQLAlchemy()
app = create_test_app()


@app.route("/", methods=['GET', 'POST'])
def message():
    return "hello!"

#TODO
# create hash manually
# compare it with password
# add some record to the database with hashed password. method
# create test to get JWT base on login and password
# create method to get JWT
# add JWT to cookies
# check cookies inside other microsrvices

if __name__ == '__main__':
    app.run(debug=True, port=8810)