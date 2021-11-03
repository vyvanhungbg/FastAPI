from pydantic import  BaseModel
from .database import Base
from typing import List, Optional


class Blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blog : List[Blog]  = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title :str
    body:str
    creator:ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None