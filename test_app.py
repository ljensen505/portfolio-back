from pprint import pprint

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    body: dict[str, str] = response.json()
    welcome = body["welcome"]
    version = body["version"]
    major, minor, patch = version.split(".")
    routes = body["routes"]
    assert welcome == "backend api for lucasjensen.me"
    for v in [major, minor, patch]:
        assert v.isnumeric()
    assert len(routes) >= 3


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
