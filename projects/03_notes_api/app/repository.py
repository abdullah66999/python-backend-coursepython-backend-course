from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Note
from .schemas import NoteCreate


def create(session: Session, payload: NoteCreate) -> Note:
    note = Note(title=payload.title, text=payload.text)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note


def get(session: Session, note_id: int) -> Note | None:
    return session.scalar(select(Note).where(Note.id == note_id))


def delete(session: Session, note: Note) -> None:
    session.delete(note)
    session.commit()
