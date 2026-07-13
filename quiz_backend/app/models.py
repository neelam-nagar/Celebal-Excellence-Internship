"""
SQLAlchemy ORM models: Question and Choice.

Relationship:
    One Question  -> Many Choices
    One Choice    -> One Question
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, nullable=False)
    category = Column(String, nullable=True, index=True)

    choices = relationship(
        "Choice",
        back_populates="question",
        cascade="all, delete-orphan",
    )


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)

    question = relationship("Question", back_populates="choices")
