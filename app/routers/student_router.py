from fastapi import APIRouter, HTTPException

from app.schemas.student_schema import (
    StudentCreate,
    StudentResponse,
    StudentUpdate
)

router = APIRouter()

students = []

next_student_id = 1


@router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):
    global next_student_id

    new_student = {
        "id": next_student_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)

    next_student_id += 1

    return new_student


@router.get("/students", response_model=list[StudentResponse])
def get_students():
    return students


@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate):
    for existing_student in students:
        if existing_student["id"] == student_id:
            existing_student["name"] = student.name
            existing_student["age"] = student.age
            existing_student["course"] = student.course

            return existing_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(index)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


  #  uvicorn app.main:app --reload