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

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.auth import _check_password, create_token, has_admin_password_set
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


class LoginRequest(BaseModel):
    password: str


@app.post("/admin/login", tags=["Auth"])
def admin_login(payload: LoginRequest):
    """
    Everyone can play the quiz (GET endpoints are public). Only whoever
    knows the admin password (set via `set_admin_password.py`) can log
    in here to get a signed, 24-hour token for write access.
    """
    if not has_admin_password_set():
        raise HTTPException(
            status_code=503,
            detail="No admin password has been set yet. Run 'python set_admin_password.py' on the server first.",
        )
    if not _check_password(payload.password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    token, expires_at = create_token()
    return {"token": token, "expires_at": expires_at}
