from fastapi.testclient import TestClient
from infrastructure.api.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    assert response.status_code == 201
