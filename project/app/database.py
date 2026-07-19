"""
Database configuration for the Quiz Backend Management API.

Uses SQLite by default (zero setup, file-based). To switch to
MySQL/PostgreSQL, just change SQLALCHEMY_DATABASE_URL below, e.g.:

    PostgreSQL: "postgresql://user:password@localhost:5432/quizdb"
    MySQL:      "mysql+pymysql://user:password@localhost:3306/quizdb"
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./quiz.db"

# check_same_thread is only needed for SQLite
connect_args = {"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """FastAPI dependency that provides a DB session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
