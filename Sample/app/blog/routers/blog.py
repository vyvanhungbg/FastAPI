from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import models, schemas, oauth2
from blog.database import get_db
from ..repository import blog
router = APIRouter(prefix= '/blog', tags= ['blogs'])

@router.get('', response_model=List[schemas.ShowBlog])
def get_all(db : Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/{id}', status_code= 200, response_model= schemas.ShowBlog)
def get_all(id,  db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} not found'}
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'Blog with the id = {id} not found')
    return blog

@router.delete('/{id}', status_code= 204)
def destroy(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)\
        .delete(synchronize_session = False)
    db.commit()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} not found'}
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'Blog with the id = {id} can not delete ')
    return {'detail':'done'}

@router.put('/{id}',status_code= 202)
def update_blog(id, request: schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'Blog with the id = {id} can no')
    blog.update(request.dict())
    db.commit()
    return {'detail': 'update'}

