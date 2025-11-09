from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Column, Integer, String, Text,Boolean


DATABASE_URI = 'postgresql://postgres:evoqins2025@localhost:5432/cyb'

HEAD
DATABASE_URL = "sqlite:///./notes.db"  # SQLite file-based DB

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # Required for SQLite
)

engine = create_engine(DATABASE_URI)
d011aa04db99800e13e5c122bf59a37e161aadb6

session = Session(engine)


Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=True)
    is_active = Column(Boolean,default=True)

print("Creating Tables")
Base.metadata.create_all(bind=engine)

print("Finished Creating Tables")




