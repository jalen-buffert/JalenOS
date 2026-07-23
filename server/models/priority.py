from fastapi import FastAPI
from pydantic import BaseModel

class Priority(BaseModel):
    title: str
    category: str 
    action: str
    status: str
    importance: str 
    link: str | None = None