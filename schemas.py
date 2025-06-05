from pydantic import BaseModel, EmailStr


class Todo(BaseModel): 
    title: str 
    description: str 

class TodoUpdate(BaseModel): 
    title: str 
    description: str 

class CreateUser(BaseModel): 
    username: str 
    email: EmailStr
    password: str 

class UserOut(BaseModel): 
    username: str 
    email: EmailStr 

class LoginUser(BaseModel): 
    email: EmailStr 
    password: str 

class TokenData(BaseModel): 
    id: str 



