import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    data = rv.get_json()
    assert "service" in data
    assert "version" in data
    assert "hostname" in data

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.get_json() == {"status": "ok"}

def test_greeting_default(client):
    rv = client.get('/greeting')
    assert rv.status_code == 200
    assert rv.get_json() == {"greeting": "Hello, world!"}

def test_greeting_feature_flag_on(monkeypatch, client):
    monkeypatch.setenv("FEATURE_NEW_GREETING", "true")
    rv = client.get('/greeting')
    assert rv.status_code == 200
    assert rv.get_json() == {"greeting": "Hello from new feature!"}
