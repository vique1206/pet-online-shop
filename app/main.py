from fastapi import FastAPI
from app.database import engine, Base
from app.models import User, Product

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Добро пожаловать!"}