from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas,models,database
from  .schemas import Blog
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog', response_model=List[schemas.ShowBlog])
def get_all(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code= 200, response_model= schemas.ShowBlog)
def get_all(id, response: Response, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} not found'}
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'Blog with the id = {id} not found')
    return blog

@app.delete('/blog/{id}', status_code= 204)
def destroy(id, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)\
        .delete(synchronize_session = False)
    db.commit()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} not found'}
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'Blog with the id = {id} can not delete ')
    return {'detail':'done'}

@app.put('/blog/{id}',status_code= 202)
def update_blog(id,request: schemas.Blog, db : Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'Blog with the id = {id} can no')
    blog.update(request.dict())
    db.commit()
    return {'detail': 'update'}


pwd_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

@app.post('/user')
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    hashedPassword = pwd_context.hash(request.password)
    new_user = models.User(name = request.name, email = request.email, password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request