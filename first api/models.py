from database import Base
from sqlalchemy import Column, Integer, String, Float

class Expense(Base):
    __tablename__="expenses"

    id=Column(Integer,primary_key=True,index=True)
    category=Column(String)
    price=Column(Float)
    date=Column(String)
    

