from fastapi import FastAPI, Depends, HTTPException
from book_models import BookStore,session
app = FastAPI(title="Simple Notepad API")

# API to add a new book

# API to read all available books

# API to read book from a specific genre

#  API to delete a book with ID







# book = BookStore(title="a")
# session.add(book)
# session.commit()