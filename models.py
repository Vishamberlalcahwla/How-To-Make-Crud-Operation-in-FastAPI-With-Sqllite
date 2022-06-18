from .database import *
from sqlalchemy import Column,Integer,String

class Student(Base):
    __tablename__="Students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    fathername = Column(String, index=True) 
    country = Column(String, index=True)
    City= Column(String, index=True)
