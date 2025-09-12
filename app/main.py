from fastapi import FastAPI
from app.database import Base, engine, SessionLocal
from app.models import User, Product
from app.auth import hash_password

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

@app.post("/register")
def register_user(username: str, email: str, password: str):
    db = SessionLocal()
    hashed = hash_password(password)
    user = User(username=username, email=email, password_hash=hashed)
    
    db.add(user)
    db.commit()
    return user