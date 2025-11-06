from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from models import Note, engine, session

app = FastAPI(title="Simple Notes API")

# Pydantic Schemas
class NoteCreate(BaseModel):
    title: str
    content: Optional[str] = None


class NoteResponse(BaseModel):
    id: int
    title: str
    content: Optional[str]



# Create Note
@app.post("/notes", response_model=NoteResponse)
def create_note(note: NoteCreate):
    new_note = Note(title=note.title, content=note.content)
    session.add(new_note)
    session.commit()
    session.refresh(new_note)
    return new_note


# Read All Notes
@app.get("/notes", response_model=List[NoteResponse])
def get_notes():
    return session.query(Note).all()


# Read Single Note by ID
@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):
    note = session.query(Note).filter(Note.id == note_id).first()
    if not note:
        return JSONResponse({"status_code":404, "detail":"Note not found"},status_code=404)
    return note
    


# Update Note
@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_data: NoteCreate):
    note = session.query(Note).filter(Note.id == note_id).first()
    if not note:
        return JSONResponse({"status_code":404, "detail":"Note not found"},status_code=404)
    note.title = note_data.title
    note.content = note_data.content
    session.commit()
    session.refresh(note)
    return note


# Delete Note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    note = session.query(Note).filter(Note.id == note_id).first()
    if not note:
        return JSONResponse({"status_code":404, "detail":"Note not found"},status_code=404)
    session.delete(note)
    session.commit()
    return {"message": f"Note {note_id} deleted successfully"}
