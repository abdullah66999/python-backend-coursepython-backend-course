from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_create_and_redirect():
    response = client.post("/links", json={"url": "https://example.com"})
    assert response.status_code == 201
    key = response.json()["key"]
    redirect = client.get(f"/r/{key}", follow_redirects=False)
    assert redirect.status_code == 307
    assert redirect.headers["location"] == "https://example.com/"


def test_unknown_key_is_404():
    assert client.get("/r/missing").status_code == 404
