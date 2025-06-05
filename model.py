from database import Base 
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime 


class Todo(Base): 
    __tablename__ = 'Todo'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, nullable=False, default=False)
    created_date = Column(DateTime, default=datetime.utcnow)

# user 
class User(Base): 
    __tablename__ = 'users'
    id = Column(Integer, index=True, primary_key=True)
    username = Column(String, nullable=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    
