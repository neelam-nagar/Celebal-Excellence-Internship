"""
Quiz Backend Management API
============================
A FastAPI application for creating and managing quiz questions and
answer choices, with relationships maintained via SQLAlchemy ORM and
data validation via Pydantic.

Run locally:
    uvicorn app.main:app --reload

Then open http://127.0.0.1:8000/docs for interactive Swagger UI.
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import choices, questions
from pathlib import Path


# Create all tables on startup (for SQLite / quick dev use).
# For production, use Alembic migrations instead.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quiz Backend Management API",
    description=(
        "A RESTful backend for creating and managing quiz questions and "
        "answer choices, built with FastAPI, SQLAlchemy, and Pydantic."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev-friendly; restrict to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions.router)
app.include_router(choices.router)


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_FILE = BASE_DIR / "frontend" / "index.html"

@app.get("/", include_in_schema=False)
def root():
    if FRONTEND_FILE.exists():
        return FileResponse(FRONTEND_FILE)
    return {
        "message": "Quiz Backend Management API is running",
        "docs": "/docs",
    }
