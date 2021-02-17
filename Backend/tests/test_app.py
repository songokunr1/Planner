import json

import requests

from Backend.app import app
from Backend import create_test_app
import pytest


# @pytest.fixture
# def app():
#     app = create_test_app()
#     yield app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_empty_db():
    """Start with a blank database."""
    app.testing = True
    response = requests.get("http://127.0.0.1:8030")
    print(response)
    assert response.status_code == 200


def test_login():
    """Start with a blank database."""
    app.testing = True
    response = requests.get("http://127.0.0.1:8030/login")
    print(response)
    assert response.status_code == 404


def test_post():
    json_data = {
        "name": "ivanleoncz",
        "role": "Software Developer"
    }

    headers = {'content-type': 'application/json'}
    r = requests.post(
        'http://127.0.0.1:8030/message', headers=headers, data=json.dumps(json_data)
    )

class TestSomethings:
    def test_post_2(self, client):
        r = client.get("/")
        assert r.status_code == 201