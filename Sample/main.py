from fastapi import FastAPI
from typing import Optional
from pydantic import  BaseModel
app = FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published: Optional[bool]


@app.get('/')
def index():
    return  {'data':{'blog list'}}

@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}


@app.get('/blog')
def getBlog(limit=10,published = True, sort: Optional[str] = None):
    if published:
        return {'data':f'{limit} publised blogs from the db'}

@app.get('/blog')
def getBlog(limit):
    return {'data':f'{limit} blogs from the db'}

@app.post('/blog')
def create_blog(request: Blog):
    return  request
    return {'data': 'Blog is created'}

