from pydantic import BaseModel

class Priority(BaseModel):
    priority_id: str | int
    title: str
    category: str 
    action: str
    status: str
    importance: str 
    link: str | None = None
    
class PriorityCreate(BaseModel):
    title: str
    category: str
    status: str | None = None
    importance: str