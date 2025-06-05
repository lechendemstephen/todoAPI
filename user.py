from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import database, schemas, utils, model, Oath2

router = APIRouter(
    tags=['Authentication'], 
    prefix='/user'
)


# create a user 
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user:schemas.CreateUser,  db: Session = Depends(database.get_db)): 
    # hashing the password from user 
    hashed_password = utils.hash_password(user.password)
    # attributing the hashed password back to the user 
    user.password = hashed_password 

    new_user = model.User(
        **user.dict() 
    )

    db.add(new_user)
    db.commit() 
    db.refresh(new_user)

    return new_user

# login user 
@router.post('/login', status_code=status.HTTP_200_OK)
def login_user(user: schemas.LoginUser,  db: Session = Depends(database.get_db)): 
    db_user = db.query(model.User).filter(model.User.email == user.email).first() 
    if not db_user: 
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'no user found with email: {user.email}, create an account')
    if not utils.verify_password(user.password, db_user.password): 
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'invalid login credentials')
    
    access_token = Oath2.create_access_token({"user_id": db_user.id})

    return access_token 
