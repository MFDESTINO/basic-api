from fastapi.testclient import TestClient
import pytest
from main import app

@pytest.mark.skip(reason="will fail if user already exists.")
def test_create_user():
    """Create a new user"""

    with TestClient(app) as client:
        response = client.post(
            "/user/",
            json={
                    "username": "MFDOOM",
                    "email": "mfdoom@gmail.com",
                    "name": "Daniel Dumile",
                    "birthday": "1971-7-13"
                },
        )
        assert response.status_code == 201
        
def test_create_user_invalid_username():
    """Create a new user with a invalid username"""

    with TestClient(app) as client:
        response = client.post(
            "/user/",
            json={
                    "username": "MFDOOM_",
                    "email": "mfdoom@gmail.com",
                    "name": "Daniel Dumile",
                    "birthday": "1971-7-13"
                },
        )
        assert response.status_code == 400
        assert response.json() == {
            "detail": "Invalid username."
        }

def test_create_user_invalid_email():
    """Create a new user with a invalid email"""

    with TestClient(app) as client:
        response = client.post(
            "/user/",
            json={
                    "username": "MFDOOM",
                    "email": "mfdoomgmail.com",
                    "name": "Daniel Dumile",
                    "birthday": "1971-7-13"
                },
        )
        assert response.status_code == 400
        assert response.json() == {
            "detail": "Invalid email address."
        }

def test_create_user_invalid_birthday():
    """Create a new user with a invalid birthday"""

    with TestClient(app) as client:
        response = client.post(
            "/user/",
            json={
                    "username": "MFDOOM",
                    "email": "mfdoom@gmail.com",
                    "name": "Daniel Dumile",
                    "birthday": "1971-2-30"
                },
        )
        assert response.status_code == 400
        assert response.json() == {
            "detail": "Invalid birthday, should be YYYY-MM-DD"
        }