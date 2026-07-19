from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/choices", tags=["Choices"])


@router.post("", response_model=schemas.Choice, status_code=201)
def create_choice(choice: schemas.ChoiceCreate, db: Session = Depends(get_db)):
    """Add a new answer choice to a question."""
    db_choice = crud.create_choice(db, choice)
    if db_choice is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_choice


@router.get("", response_model=List[schemas.Choice])
def read_choices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all answer choices. Public — no login needed."""
    return crud.get_choices(db, skip=skip, limit=limit)


@router.get("/{choice_id}", response_model=schemas.Choice)
def read_choice(choice_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific answer choice by ID. Public — no login needed."""
    db_choice = crud.get_choice(db, choice_id)
    if db_choice is None:
        raise HTTPException(status_code=404, detail="Choice not found")
    return db_choice


@router.put("/{choice_id}", response_model=schemas.Choice)
def update_choice(choice_id: int, choice: schemas.ChoiceUpdate, db: Session = Depends(get_db)):
    """Update an answer choice."""
    db_choice = crud.update_choice(db, choice_id, choice)
    if db_choice is None:
        raise HTTPException(status_code=404, detail="Choice not found")
    return db_choice


@router.delete("/{choice_id}", status_code=204)
def delete_choice(choice_id: int, db: Session = Depends(get_db)):
    """Delete an answer choice."""
    deleted = crud.delete_choice(db, choice_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Choice not found")
    return None
