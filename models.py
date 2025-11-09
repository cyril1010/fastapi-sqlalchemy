from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Column, Integer, String, Text



DATABASE_URL = "sqlite:///./notes.db"  # SQLite file-based DB

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # Required for SQLite
)

session = Session(engine)


Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=True)

print("Creating Tables")
Base.metadata.create_all(bind=engine)
print("Finished Creating Tables")




