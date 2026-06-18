from fastapi import FastAPI

from models import EntryRequest
from markdown_service import save_entry

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Riyaz"
    }


@app.post("/entry")
def create_entry(entry: EntryRequest):

    file_path = save_entry(entry.content)

    return {
        "message": "Entry Saved",
        "file": file_path
    }