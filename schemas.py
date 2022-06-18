from lib2to3.pytree import Base
from pydantic import BaseModel


class StudentCreate(BaseModel):
    id : int
    name :str
    fathername : str
    country : str
    City : str

    class Config:
        orm_mode = True


class student_list(BaseModel):
    id : int
    name :str
    fathername : str
    country : str
    City : str
    class Config:
        orm_mode = True           

