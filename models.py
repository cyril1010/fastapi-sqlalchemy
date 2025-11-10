from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Column, Integer, String, Text,Boolean


DATABASE_URI = 'postgresql://postgres:akzpass@localhost:5432/akshay'


# DATABASE_URL = "sqlite:///./notes.db"  # SQLite file-based DB

engine = create_engine(
    DATABASE_URI, connect_args={"check_same_thread": False}  # Required for SQLite
)

engine = create_engine(DATABASE_URI)


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




