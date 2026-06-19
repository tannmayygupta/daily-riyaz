from fastapi import FastAPI
from git_service import commit_and_push
from models import EntryRequest
from markdown_service import save_entry
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Riyaz"
    }


@app.post("/entry")
def create_entry(entry: EntryRequest):

    file_path = save_entry(entry.content)

    commit_and_push(
        f"Riyaz Entry - {file_path}"
    )

    return {
        "message": "Entry Saved",
        "file": file_path
    }