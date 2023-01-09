from fastapi.testclient import TestClient

from main import app


def test_create_user():
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
        
def test_create_invalid_username():
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