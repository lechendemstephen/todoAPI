from fastapi import FastAPI 
import todo, user
from database import engine
import model


model.Base.metadata.create_all(bind=engine)

app = FastAPI() 



app.include_router(todo.router)
app.include_router(user.router)