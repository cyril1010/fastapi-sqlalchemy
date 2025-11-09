

# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import *
from pydantic_validations import *
import operations

app = FastAPI(title="Simple Notepad API")




@app.post("/notes/")
def create_note(note: NoteCreate):
    return operations.create_note(note)


@app.get("/notes/")
def list_notes():
    return operations.get_notes()


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    success = operations.delete_note(note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}

