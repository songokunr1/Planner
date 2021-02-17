db = SQLAlchemy()

def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "xxxxxxtestdatabasexxx"
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push() # this does the binding
    return app

from flask.ext.testing import TestCase
from myapp import create_app, db

class MyTest(TestCase):

    # I removed some config passing here
    def create_app(self):
        return create_test_app()

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()