import sys
import os
import pytest

#Add project root to Python path so we can import app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#Import the Flask app object from app.py
import app

#Dummy test to verify pytest setup
def test_hello():
    print("Running test_hello...")
    assert True  # Always passes

#Functional test: checks if the root endpoint returns status 200
def test_client():
    print("Starting test_client...")

    # Create a test client using Flask's built-in method
    with app.app.test_client() as client:
        response = client.get("/")
        print("Response status code:", response.status_code)
        print("Response data:", response.data.decode())

        # Assert that the response code is HTTP 200 OK
        assert response.status_code == 200
