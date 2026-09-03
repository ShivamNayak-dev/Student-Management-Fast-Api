from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    age: int
    course: str


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str