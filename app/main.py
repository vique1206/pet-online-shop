from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine, SessionLocal
from app.models import User, Product
from app.auth import hash_password

Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def root(request: Request):
    db = SessionLocal()
    products = db.query(Product).all()
    print(len(products))
    db.close()
    return templates.TemplateResponse("products.html", {"request": request,"products": products})

@app.get("/registration")
def register_page(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})

@app.post("/register")
def register_user(username: str = Form(...), password: str = Form(...)):
    db = SessionLocal()
    hashed = hash_password(password)
    user = User(username=username, password_hash=hashed)
    
    db.add(user)
    db.commit()
    return {"message": "ok"}