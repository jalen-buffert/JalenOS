from typing import List 
from typing import Optional
from typing import Annotated
from typing import TypeVar
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import types
import uuid
import enum

class Base(DeclarativeBase):
    pass

class Category(enum.Enum):
    CAREER = 'Career'
    INVESTMENT = 'Investment'
    EDUCATION = 'Education'
    PROJECT = 'Project'
    MEALTH = 'Health'
    
class Importance(enum.Enum):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

class Priority(Base):
    __tablename__ = "priorities"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(35))
    category: Mapped[Category]
    action: Mapped[str] = mapped_column(String(200))
    status: Mapped[Optional[str]]
    importance: Mapped[Importance]
    link: Mapped[Optional[str]]
    
    def __repr__(self) -> str: 
        return f"Priority(id={self.id}, title={self.title}, category={self.category}, status={self.status})"
    
    