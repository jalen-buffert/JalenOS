from pydantic import BaseModel, Field

class Priority(BaseModel):
    priority_id: str 
    title: str = Field(default = None, title= "Very brief description of priority", max_length=50)
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
    
class PriorityUpdate(BaseModel):
    title: str | None = None
    action: str | None = None
    status: str | None = None
    importance: str | None = None 
    link: str | None = None