from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()

@app.post('/students/', response_model=schemas.StudentCreate)
def create_user(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, Student=student)

@app.get('/studentslist/', response_model=List[schemas.student_list])
def read_student_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.get('/get_student/{student_id}', response_model=schemas.StudentCreate)
def read_user(student_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_student_by_id(db, student_id=student_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Student not found.")
    return db_user

@app.post('/delete_student/{student_id}', response_model=schemas.StudentCreate)
def delete_student_by_id(student_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_student_by_id(db, student_id=student_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Student not found.")
    return db_user

