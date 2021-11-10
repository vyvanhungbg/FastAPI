from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import models, schemas
from blog.database import get_db
from blog.hashing import Hash

router = APIRouter(tags= ['users'])


@router.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db : Session = Depends(get_db)):

    new_user = models.User(name = request.name, email = request.email, password = Hash.bcryt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id:int ,db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    return user