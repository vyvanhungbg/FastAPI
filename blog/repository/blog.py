from fastapi import Depends
from sqlalchemy.orm import Session

from .. import models
from blog.database import get_db


def get_all(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs