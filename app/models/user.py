from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable = False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    
    def verify_password(self, password: str) -> bool:
        return
        
    def __repr__(self):
        return f"<User(username={self.username},email={self.email})>"