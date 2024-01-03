from fastapi.testclient import TestClient

from helpers import get_token
from main import app

client = TestClient(app)
token = get_token()


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


def test_project():
    response = client.get("/projects/1")
    assert response.status_code == 200
    body = response.json()
    vals = ["id", "name", "description"]  # remaining vals are optional
    assert all([k in body for k in vals])


def test_post_projects():
    project = {
        "name": "test project",
        "description": "test description",
        "source": "github.com/test",
        "live": "test.com",
    }
    response = client.post(
        "/projects",
        json=project,
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 201
    p_id = response.json()["id"]

    response = client.get("/projects")
    assert response.status_code == 200
    body = response.json()
    assert any([p.get("id") == p_id for p in body])

    response = client.get(f"/projects/{p_id}")
    assert response.status_code == 200
    body = response.json()

    assert body["name"] == project["name"]
    assert body["description"] == project["description"]
    assert body["source"] == project["source"]
    assert body["live"] == project["live"]
    assert body["id"] == p_id


def test_delete_project():
    response = client.get("/projects")
    assert response.status_code == 200
    body = response.json()
    p_id = body[-1]["id"]

    response = client.delete(
        f"/projects/{p_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 204

    response = client.get("/projects")
    assert response.status_code == 200
    body = response.json()
    assert not any([p.get("id") == p_id for p in body])
