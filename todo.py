from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, model, Oath2
from sqlalchemy.orm import Session

router = APIRouter(
    tags= ['Todo'],
    prefix='/todo'
) 

# getting all the todos from the database

@router.get('/')
def get_todo(db: Session = Depends(database.get_db), logged_user: int = Depends(Oath2.current_user)): 
    all_todo = db.query(model.Todo).all()

    return all_todo

# create new todo 

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.Todo, db: Session = Depends(database.get_db), logged_user: int = Depends(Oath2.current_user)): 
    new_todo = model.Todo(
        **todo.dict()
    )


    db.add(new_todo)
    db.commit() 
    db.refresh(new_todo)
  

    return new_todo 

# retrieve a particular post 
@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_single_todo(id: int, db: Session = Depends(database.get_db), logged_user: int = Depends(Oath2.current_user)): 
    single_todo = db.query(model.Todo).filter(model.Todo.id == id).first() 

    if not single_todo: 
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no todo found with id {id}')
    
    return single_todo 

# update a single todo 
@router.put('/{id}', status_code=status.HTTP_201_CREATED)
def update_todo(todo_schema: schemas.TodoUpdate , id:int, db: Session = Depends(database.get_db), logged_user: int = Depends(Oath2.current_user)): 
    single_todo = db.query(model.Todo).filter(model.Todo.id == id).first() 

    if not single_todo: 
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no todo found with id: {id}')
    
    for key, value in todo_schema.dict(exclude_unset=True).items(): 
        if value is not None: 
            setattr(single_todo, key, value)
    db.commit() 
    db.refresh(single_todo)

    return single_todo

# delete single todo 
@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_todo(id: int, db: Session = Depends(database.get_db), logged_user: int = Depends(Oath2.current_user)): 
    single_todo = db.query(model.Todo).filter(model.Todo.id == id ).first() 

    if not single_todo: 
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no todo found with id: {id}')
    db.delete(single_todo)
    db.commit() 

    return {
        "message": f"todo {single_todo}, successfully deleted"
    }
