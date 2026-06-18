from pydantic import BaseModel

class EntryRequest(BaseModel):
    content: str