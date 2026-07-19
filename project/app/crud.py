"""
Business logic / CRUD layer. Keeps route handlers thin and database
operations reusable and testable.
"""

from typing import Optional

from sqlalchemy.orm import Session

from app import models, schemas


# ---------- Question CRUD ----------

def create_question(db: Session, question: schemas.QuestionCreate) -> models.Question:
    db_question = models.Question(
        question_text=question.question_text,
        category=question.category,
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_question(db: Session, question_id: int) -> Optional[models.Question]:
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def get_questions(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
):
    query = db.query(models.Question)
    if category:
        query = query.filter(models.Question.category == category)
    return query.offset(skip).limit(limit).all()


def update_question(
    db: Session, question_id: int, question: schemas.QuestionUpdate
) -> Optional[models.Question]:
    db_question = get_question(db, question_id)
    if not db_question:
        return None
    update_data = question.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_question, field, value)
    db.commit()
    db.refresh(db_question)
    return db_question


def delete_question(db: Session, question_id: int) -> bool:
    db_question = get_question(db, question_id)
    if not db_question:
        return False
    db.delete(db_question)  # cascade deletes associated choices
    db.commit()
    return True


# ---------- Choice CRUD ----------

def create_choice(db: Session, choice: schemas.ChoiceCreate) -> Optional[models.Choice]:
    # Ensure the parent question exists
    if not get_question(db, choice.question_id):
        return None
    db_choice = models.Choice(
        choice_text=choice.choice_text,
        is_correct=choice.is_correct,
        question_id=choice.question_id,
    )
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice


def get_choice(db: Session, choice_id: int) -> Optional[models.Choice]:
    return db.query(models.Choice).filter(models.Choice.id == choice_id).first()


def get_choices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Choice).offset(skip).limit(limit).all()


def update_choice(
    db: Session, choice_id: int, choice: schemas.ChoiceUpdate
) -> Optional[models.Choice]:
    db_choice = get_choice(db, choice_id)
    if not db_choice:
        return None
    update_data = choice.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_choice, field, value)
    db.commit()
    db.refresh(db_choice)
    return db_choice


def delete_choice(db: Session, choice_id: int) -> bool:
    db_choice = get_choice(db, choice_id)
    if not db_choice:
        return False
    db.delete(db_choice)
    db.commit()
    return True
