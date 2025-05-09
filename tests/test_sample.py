import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from unittest.mock import MagicMock

from app.main import app  # Adjust if your FastAPI app is elsewhere
from app.db import crud
from app.api.v1.endpoints import sample

# Override dependencies
def override_get_db():
    db = MagicMock(spec=Session)
    db.close = MagicMock()
    yield db

def override_verify_api_key():
    return "test-api-key"

app.dependency_overrides[sample.get_db] = override_get_db
app.dependency_overrides[sample.verify_api_key] = override_verify_api_key

client = TestClient(app)

def test_hello_success(monkeypatch):
    test_payload = {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30
    }

    # Mock the create_user function
    def mock_create_user(db, name, email, age):
        return {"name": name, "email": email, "age": age}
    
    monkeypatch.setattr(crud, "create_user", mock_create_user)

    response = client.post("/api/v1/hello", json=test_payload)
    assert response.status_code == 200
    assert "Hello, John Doe!" in response.json()["message"]

def test_hello_email_conflict(monkeypatch):
    test_payload = {
        "name": "Jane",
        "email": "jane@example.com",
        "age": 25
    }

    # Simulate DB exception
    def mock_create_user(db, name, email, age):
        raise Exception("Unique constraint failed")

    monkeypatch.setattr(crud, "create_user", mock_create_user)

    response = client.post("/api/v1/hello", json=test_payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Could not save user. Email might already exist."
