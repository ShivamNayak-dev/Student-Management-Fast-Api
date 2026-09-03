from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    course: str


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/about")
def about():
    return {"message": "This is the Student Management API"}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }


@app.get("/search")
def search_students(name: str | None = None, age: int | None = None):
    return {
        "name": name,
        "age": age
    }


@app.post("/students")
def create_student(student: Student):
    return student