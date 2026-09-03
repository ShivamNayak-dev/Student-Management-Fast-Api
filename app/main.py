from fastapi import FastAPI

from app.routers.student_router import router as student_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/about")
def about():
    return {"message": "This is the Student Management API"}


app.include_router(student_router)