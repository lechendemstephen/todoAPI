from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Finalbaba1@localhost:65432/todo'




engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base() 


# creating the database 
def get_db(): 
    db = sessionLocal() 
    try: 
        yield db 
    finally: 
        db.close() 




