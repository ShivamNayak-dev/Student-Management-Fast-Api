# 🎓 Student Management API

A foundational CRUD backend for managing student records, built with **Python / FastAPI / Pydantic / Uvicorn**.

This is a first-principles FastAPI project designed to build a strong understanding of backend and REST API fundamentals before moving into more advanced concepts such as SQLAlchemy, PostgreSQL, authentication, testing, Docker, Redis, background jobs, and production architecture.

The project focuses on understanding how a FastAPI application receives HTTP requests, validates input, routes requests to the correct handler, processes data, handles errors, and returns structured HTTP responses.

The application currently uses an **in-memory Python list** as temporary storage. Database integration is intentionally left for a later project so that the API fundamentals can be understood independently before introducing persistence and database architecture.

---

## 🎯 Project Purpose

The primary goal of this project is to learn and practice the fundamentals of building REST APIs with FastAPI.

Rather than immediately introducing databases, authentication, repositories, services, Docker, and other advanced backend concepts, this project focuses on getting the core request/response lifecycle correct.

The project covers:

- FastAPI application creation
- API routing
- HTTP methods
- REST principles
- Path parameters
- Query parameters
- Request bodies
- Pydantic models
- Request validation
- Response models
- CRUD operations
- HTTP status codes
- Error handling
- APIRouter
- Modular project structure
- Automatic API documentation
- API testing with Postman
- Running FastAPI with Uvicorn
- Git and GitHub based development

The project acts as the foundation for the larger FastAPI backend projects that follow.

---

## 🧱 What This Project Demonstrates

| Concern | How It's Handled |
|---|---|
| FastAPI application setup | `FastAPI()` creates the application instance |
| HTTP routing | FastAPI decorators such as `@app.get()`, `@router.post()`, etc. |
| Modular routing | Student endpoints are separated into `student_router.py` |
| Request validation | Pydantic `BaseModel` validates incoming JSON data |
| Request contracts | `StudentCreate` and `StudentUpdate` define expected request data |
| Response contracts | `StudentResponse` defines the structure returned to clients |
| CRUD operations | Create, Read, Update, and Delete endpoints are implemented |
| Path parameters | `/students/{student_id}` identifies a specific student |
| Query parameters | `/search?name=...&age=...` demonstrates optional filtering inputs |
| Error handling | `HTTPException` is used for cases such as missing students |
| API documentation | FastAPI automatically generates Swagger UI and ReDoc |
| API testing | Endpoints can be tested through Postman and `/docs` |
| Temporary persistence | Python list is used as an in-memory data store |
| Application server | Uvicorn runs the FastAPI application |
| Version control | Git commits and GitHub are used throughout development |

---

# 🏗️ Architecture

The project intentionally uses a simple architecture appropriate for a first FastAPI project.

```text
                     HTTP Request
                          |
                          v
                +-------------------+
                |     FastAPI       |
                |    Application    |
                +-------------------+
                          |
                          v
                +-------------------+
                |   Student Router  |
                | student_router.py |
                +-------------------+
                          |
                          v
                +-------------------+
                |     Pydantic      |
                | Request / Response|
                |      Schemas      |
                +-------------------+
                          |
                          v
                +-------------------+
                |  CRUD Application |
                |      Logic        |
                +-------------------+
                          |
                          v
                +-------------------+
                | In-Memory List    |
                |   students = []   |
                +-------------------+
                          |
                          v
                     HTTP Response

A future production-style architecture will evolve toward:

Client
  |
  v
FastAPI Router
  |
  v
Service Layer
  |
  v
Repository Layer
  |
  v
SQLAlchemy
  |
  v
PostgreSQL


Additional cross-cutting concerns can then be introduced around this architecture:

Authentication
Authorization
Validation
Exception Handling
Logging
Configuration
Testing
Caching
Background Jobs
Message Queues
Docker
CI/CD
Observability
Cloud Deployment
