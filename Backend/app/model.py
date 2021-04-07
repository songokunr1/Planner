from datetime import datetime

from sqlalchemy.orm import backref

from .app import db # login_manager
from flask_login import UserMixin, current_user
from sqlalchemy.dialects.postgresql.json import JSONB
# from app.helpers import get_date_info


class Calendar(db.Model):
    __tablename__ = 'Calendar'
    id =
    date = db.Column(db.String(100), nullable=False, default=datetime.utcnow)
    year =
    month =
    day =
    week =

class TimeFrame(db.Model):
    __tablename__ = 'TimeFrame'
    id =
    hour_from =
    minute_from =
    hour_to =
    minute_to =

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
