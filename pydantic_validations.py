from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str | None = None

class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int