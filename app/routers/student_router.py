from fastapi import APIRouter

from app.schemas.student_schema import StudentCreate

router = APIRouter()

students = []

next_student_id = 1


@router.post("/students")
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