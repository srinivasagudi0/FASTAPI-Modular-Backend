#Left at 3:28:27  secs and at Exce in https://www.youtube.com/watch?v=7t2alSnE2-I
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router, tags=["blog"])
app.include_router(user.router)

app.include_router(authentication.router)





