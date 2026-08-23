from pydantic import BaseModel, Field, AnyUrl
from typing import Union, Optional
from enum import Enum

class Category(str, Enum):
    CAREER = 'Career'
    INVESTMENT = 'Investment'
    EDUCATION = 'Education'
    PROJECT = 'Project'
    HEALTH = 'Health'
    
class Importance(str, Enum):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

class Priority(BaseModel):
    priority_id: str 
    title: str = Field(max_length=50)
    category: Category
    action: str 
    status: str = Field(max_length=200)
    importance: Importance
    link: Union[AnyUrl, None] = Field(default=None)
    
class PriorityCreate(BaseModel):
    title: str = Field(max_length=50)
    category: Category
    status:  str | None = Field(default=None,max_length=200)
    importance: Importance
    
class PriorityUpdate(BaseModel):
    title: Union[str, None] = Field(default = None, title= "Very brief description of priority", max_length=50)
    action: Union[str, None] = Field(default=None)
    status: Union[str, None] = Field(default=None, max_length=200)
    importance: Union[Importance, None] = Field(default=None)
    link: Union[AnyUrl, None] = Field(default=None)