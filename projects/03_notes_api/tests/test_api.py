from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db import Base, get_session


engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
Base.metadata.create_all(engine)


def override_session():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = override_session
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
