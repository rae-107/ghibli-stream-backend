from fastapi import FastAPI
from app.routes import users
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)