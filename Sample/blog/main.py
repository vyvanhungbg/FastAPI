from fastapi import FastAPI
from venv.app.blog import models
from venv.app.blog import engine

from venv.app.blog import blog, authentication
from venv.app.blog.routers import user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

