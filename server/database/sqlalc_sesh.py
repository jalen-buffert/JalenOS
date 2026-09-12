import sqlalchemy
from sqlalchemy import create_engine
from server.models.priority_sql import Base, Priority
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg://jalenbuffert@localhost/JalenOSdb")

Base.metadata.create_all(engine)

with Session(engine) as session:
    new_priority = Priority(
        title="Update Resume",
        action_needed="Reach out to XXX< and edit version XXX",
        category_id="1",
        importance_id="1",
        status_id="2",
    )
    
    session.add(new_priority)
    
    session.commit()


