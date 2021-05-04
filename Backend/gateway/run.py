from app import app
from flask import Flask
from app import db

from gevent.pywsgi import WSGIServer
import os

if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(port=8030, debug=True)



@app.before_first_request
def create_tables():
    db.create_all()
