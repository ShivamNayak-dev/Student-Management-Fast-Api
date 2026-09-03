from fastapi import FastAPI

app = FastAPI()


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