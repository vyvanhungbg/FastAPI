from pydantic import  BaseModel
from .database import Base


class Blog(BaseModel):
    title:str
    body:str

class ShowBlog(Blog):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str