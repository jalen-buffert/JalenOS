from pydantic import BaseModel

class Priority(BaseModel):
    priority_id: int
    title: str
    category: str 
    action: str
    status: str
    importance: str 
    link: str | None = None