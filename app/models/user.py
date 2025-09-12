import bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable = False)
    password_hash = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<User(username={self.username},id={self.id})>"