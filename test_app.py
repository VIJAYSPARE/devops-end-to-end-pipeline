# test_app.py

import pytest
from app import create_app
from urllib.parse import quote

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
 future_branch
    expected_text = quote('Hello_world this is my first cicd pipeline123')

    
 master
    assert expected_text.encode() in response.data
