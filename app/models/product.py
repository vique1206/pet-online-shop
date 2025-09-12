from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Product(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    count = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price})>"
