from typing import List, Optional, Annotated, TypeVar, Literal
from sqlalchemy import ForeignKey,String,Enum,types, ForeignKeyConstraint
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
import uuid
import enum


class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"
    
    catregory_id:Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(50))
    
    def __repr__(self) -> str:
        return f"Category(id={self.id}, category={self.category})"
        
class Importance(Base):
    __tablename__ = "importance"
    
    importance_id: Mapped[int] = mapped_column(primary_key=True)
    importance_level: Mapped[str] = mapped_column(String(50))
    
    def __repr__(self) -> str:
        return f"Importance(id={self.id}, importance={self.importance})"
    
    
class Status(Base):
    __tablename__ = "status"
    
    status_id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(50))
    
class Priority(Base):
    __tablename__ = "priorities"
    
    priority_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    action_needed: Mapped[str] = mapped_column(String(250),active_history=True)
    link: Mapped[Optional[str]]
    category_id: Mapped[int] 
    importance_id: Mapped[int]
    status_id: Mapped[int]
    ForeignKeyConstraint(["category_id", "importance_id", "status_id"],
                         ["categories.category_id","importance.importance_id", "status.status_id"]
    )
        
    def __repr__(self) -> str: 
        return f"Priority(id={self.id}, title={self.title}, category={self.category}, status={self.status})"
     