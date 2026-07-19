"""
Pydantic models used for request validation and response serialization.
"""

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


# ---------- Choice schemas ----------

class ChoiceBase(BaseModel):
    choice_text: str = Field(..., min_length=1, description="The answer option text")
    is_correct: bool = Field(default=False, description="Whether this is the correct answer")


class ChoiceCreate(ChoiceBase):
    question_id: int = Field(..., description="ID of the question this choice belongs to")


class ChoiceUpdate(BaseModel):
    choice_text: Optional[str] = None
    is_correct: Optional[bool] = None


class Choice(ChoiceBase):
    id: int
    question_id: int

    model_config = ConfigDict(from_attributes=True)


# ---------- Question schemas ----------

class QuestionBase(BaseModel):
    question_text: str = Field(..., min_length=1, description="The quiz question text")
    category: Optional[str] = Field(default=None, description="Quiz category/domain (optional)")


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    category: Optional[str] = None


class Question(QuestionBase):
    id: int
    choices: List[Choice] = []

    model_config = ConfigDict(from_attributes=True)
