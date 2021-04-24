from app import db,app
from flask_login import UserMixin, current_user
from flask_login import LoginManager

login = LoginManager(app)
login.login_view = 'login'
login.login_message_category = 'info'

@login.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()