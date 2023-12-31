from pprint import pprint

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body == {"welcome": "backend api for my portfolio"}


def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    body = response.json()
    vals = ["name", "email", "bio", "github", "linkedin"]
    assert all([k in body for k in vals])


def test_projects():
    response = client.get("/projects")
    assert response.status_code == 200
    body = response.json()
    assert len(body) > 0
    vals = ["id", "name", "description"]  # remaining vals are optional
    assert all([k in body[0] for k in vals])
