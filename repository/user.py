
from repository import models
from repository.hashing import Hash

def create(request, db):
    new_user = models.User(username=request.username, email=request.email, password=Hash.hash(request.password), disabled=request.disabled)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# def show(id, db):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
#     return user

def show_all(db):
    users = db.query(models.User).all()
    return users