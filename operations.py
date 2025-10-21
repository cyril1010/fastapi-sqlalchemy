from models import *
from pydantic_validations import *




def create_note(note: NoteCreate):
    db_note = Note(title=note.title, content=note.content)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note

def get_notes():
    return session.query(Note).all()

def delete_note(note_id: int):
    note = session.query(Note).filter(Note.id == note_id).first()
    if note:
        session.delete(note)
        session.commit()
        return True
    return False
