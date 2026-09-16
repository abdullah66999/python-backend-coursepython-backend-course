from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    text: str = Field(default="", max_length=20_000)


class NoteRead(NoteCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
