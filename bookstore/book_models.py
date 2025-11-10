from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base


DATABASE_URI = 'postgresql://postgres:evoqins2025@localhost:5432/cyb'

Base = automap_base()
engine = create_engine(DATABASE_URI)
Base.prepare(engine,reflect=True)

BookStore = Base.classes.bookstore

session = Session(engine)



print("DB Configured and Tables initialized Successfully...! ")
