from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_and_read_note():
    response = client.post("/notes", json={"title": "Первая", "text": "Текст"})
    assert response.status_code == 201
    note_id = response.json()["id"]

    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Первая"


def test_empty_title_is_rejected():
    response = client.post("/notes", json={"title": ""})
    assert response.status_code == 422


def test_missing_note_is_404():
    assert client.get("/notes/999999").status_code == 404
