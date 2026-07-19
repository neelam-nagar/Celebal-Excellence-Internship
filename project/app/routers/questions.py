from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.auth import require_admin
from app.database import get_db

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("", response_model=schemas.Question, status_code=201, dependencies=[Depends(require_admin)])
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    """Create a new quiz question. Requires admin login."""
    return crud.create_question(db, question)


@router.get("", response_model=List[schemas.Question])
def read_questions(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """Retrieve all questions, optionally filtered by category. Public — no login needed."""
    return crud.get_questions(db, skip=skip, limit=limit, category=category)


@router.get("/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific question by ID. Public — no login needed."""
    db_question = crud.get_question(db, question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@router.put("/{question_id}", response_model=schemas.Question, dependencies=[Depends(require_admin)])
def update_question(
    question_id: int, question: schemas.QuestionUpdate, db: Session = Depends(get_db)
):
    """Update an existing question. Requires admin login."""
    db_question = crud.update_question(db, question_id, question)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@router.delete("/{question_id}", status_code=204, dependencies=[Depends(require_admin)])
def delete_question(question_id: int, db: Session = Depends(get_db)):
    """Delete a question and its associated choices. Requires admin login."""
    deleted = crud.delete_question(db, question_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Question not found")
    return None
