import sqlalchemy
from sqlalchemy import create_engine
from server.models.priority_sql import Base, Priority,Category, Importance, Status 
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg://jalenbuffert@localhost/JalenOSdb")

Base.metadata.create_all(engine)

# with Session(engine) as session:
    # c1 = Category(category_id = 1, category = "Career")
    # c2 = Category(category_id = 2, category= "Investment")
    # c3 = Category(category_id = 3, category = "Education")
    # c4 = Category(category_id = 4, category = "Health")
    # c5 = Category(category_id = 5, category = "Projects")
    # i1 = Importance(importance_id = 1, importance_level = "High")
    # i2 = Importance(importance_id = 2, importance_level = "Medium")
    # i3 = Importance(importance_id = 3, importance_level = "Low")
    # s1 = Status(status_id = 1, status = "Not Started")
    # s2 = Status(status_id = 2, status = "In Progress")
    # s3 = Status(status_id = 3, status = "DND")
    # s4 = Status(status_id = 4, status = "Done")
    # session.add_all([])
    
    # session.commit()



