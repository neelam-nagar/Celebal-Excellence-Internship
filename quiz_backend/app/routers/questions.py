from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("", response_model=schemas.Question, status_code=201)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    """Create a new quiz question."""
    return crud.create_question(db, question)


@router.get("", response_model=List[schemas.Question])
def read_questions(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """Retrieve all questions, optionally filtered by category."""
    return crud.get_questions(db, skip=skip, limit=limit, category=category)


@router.get("/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific question by ID."""
    db_question = crud.get_question(db, question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@router.put("/{question_id}", response_model=schemas.Question)
def update_question(
    question_id: int, question: schemas.QuestionUpdate, db: Session = Depends(get_db)
):
    """Update an existing question."""
    db_question = crud.update_question(db, question_id, question)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@router.delete("/{question_id}", status_code=204)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    """Delete a question and its associated choices."""
    deleted = crud.delete_question(db, question_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Question not found")
    return None
