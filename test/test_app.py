import pytest
from app import app
def test_hello():
    assert True  # This is a placeholder test that always passes
def test_client():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200