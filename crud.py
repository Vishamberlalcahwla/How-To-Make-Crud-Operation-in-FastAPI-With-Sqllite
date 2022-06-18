from sqlalchemy.orm import Session
from . import models, schemas


def create_student(db: Session , Student:schemas.StudentCreate):
    db_student = models.Student(
      name = Student.name,
      fathername = Student.fathername,
      country = Student.country,
      City = Student.City
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def delete_student_by_id(db: Session, student_id: int):
    db_student = db.query(models.Student).filter_by(id=student_id).first()
    db.delete(db_student)
    db.commit()
    return db_student

