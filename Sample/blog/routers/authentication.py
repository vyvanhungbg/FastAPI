from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from blog import schemas, models
from blog.database import get_db
from blog.hashing import Hash
from blog.schemas import Token
from blog.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=['authentication'])

@router.post('/login', response_model=Token)
def login(request:OAuth2PasswordRequestForm = Depends(),  db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'User name {request.username} not found')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'Invalid password')

    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email},
    )
    return {"access_token": access_token, "token_type": "bearer"}
