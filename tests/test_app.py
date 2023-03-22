import pytest
#import json
#from app import app
from tests import tests

@pytest.fixture
def client():
    with tests.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"BookwormAI" in response.data

def test_chat_endpoint(client):
    response = client.post('/chat', data={'message': 'Rich Dad, Poor Dad'})
    assert response.status_code == 200
    
