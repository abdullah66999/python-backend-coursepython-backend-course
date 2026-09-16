from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from . import repository
from .db import create_tables, get_session
from .schemas import NoteCreate, NoteRead


app = FastAPI(title="Notes API", version="1.0.0")


@app.on_event("startup")
def startup() -> None:
    create_tables()


@app.post("/notes", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, session: Session = Depends(get_session)):
    return repository.create(session, payload)


@app.get("/notes/{note_id}", response_model=NoteRead)
def get_note(note_id: int, session: Session = Depends(get_session)):
    note = repository.get(session, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    return note


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, session: Session = Depends(get_session)) -> Response:
    note = repository.get(session, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Заметка не найдена")
    repository.delete(session, note)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
