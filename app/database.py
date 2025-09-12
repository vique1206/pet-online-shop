from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core import DATABASE_URL

engine = create_engine(
    url=DATABASE_URL,
    echo=True
)

with engine.connect() as conn:
    res = conn.execute(text("SELECT sqlite_version()"))
    print(f"{res.fetchone()}")
    
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()