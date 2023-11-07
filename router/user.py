from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from repository import schemas, models, database
from repository.hashing import Hash

get_db = database.get_db
router = APIRouter(
    tags=['Users']
)

@router.post('/create_user/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(username=request.username.lower(), email=request.email, password=Hash.hash(request.password), disabled=request.disabled)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/get_all_users/', response_model=List[schemas.ShowUser])
def show_all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users