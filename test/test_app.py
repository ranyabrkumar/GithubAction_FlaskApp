import sys
import os
import pytest

# Add the parent directory to the path so `app` can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app  # Now this will work

def test_hello():
    assert True  # Placeholder test

def test_client():
    with app.app.test_client() as client:  # Use app.app because `app` is the module and `app.app` is the Flask object
        response = client.get("/")
        assert response.status_code == 200
