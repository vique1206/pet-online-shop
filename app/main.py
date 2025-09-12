from itertools import product

from fastapi import FastAPI
from app.database import Base, engine, SessionLocal
from app.models.product import Product

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Добро пожаловать!"}

@app.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    print(len(products))
    db.close()
    return [
        {"id": p.id,
         "name": p.name,
         "price": p.price,
         "count": p.count}
        for p in products
    ]