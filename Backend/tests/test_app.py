import os
import tempfile
import pytest
import requests
from Backend.app import app

# @pytest.fixture
# def app():
#     app = app_b
#     return app

def test_empty_db():
    """Start with a blank database."""
    app.testing = True
    response = requests.get("http://127.0.0.1:8030")
    print(response)
    assert response.status_code == 201



