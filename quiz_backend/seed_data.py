"""
Populates the database with sample quiz questions across multiple
categories (General Knowledge, Programming, Mathematics, Data Science).

Run with:
    python seed_data.py
"""

from app.database import Base, SessionLocal, engine
from app.models import Choice, Question

Base.metadata.create_all(bind=engine)

SAMPLE_DATA = [
    {
        "question_text": "What is the capital of France?",
        "category": "General Knowledge",
        "choices": [
            ("Paris", True),
            ("London", False),
            ("Rome", False),
            ("Berlin", False),
        ],
    },
    {
        "question_text": "Which planet is known as the Red Planet?",
        "category": "General Knowledge",
        "choices": [
            ("Venus", False),
            ("Mars", True),
            ("Jupiter", False),
            ("Saturn", False),
        ],
    },
    {
        "question_text": "Which keyword is used to define a function in Python?",
        "category": "Programming",
        "choices": [
            ("function", False),
            ("def", True),
            ("func", False),
            ("lambda", False),
        ],
    },
    {
        "question_text": "What does 'ORM' stand for in backend development?",
        "category": "Programming",
        "choices": [
            ("Object Relational Mapping", True),
            ("Object Runtime Manager", False),
            ("Online Resource Management", False),
            ("Operational Request Model", False),
        ],
    },
    {
        "question_text": "What is the value of 7 x 8?",
        "category": "Mathematics",
        "choices": [
            ("54", False),
            ("56", True),
            ("58", False),
            ("64", False),
        ],
    },
    {
        "question_text": "Which library is commonly used for data manipulation in Python?",
        "category": "Data Science",
        "choices": [
            ("pandas", True),
            ("flask", False),
            ("requests", False),
            ("pytest", False),
        ],
    },
]


def seed():
    db = SessionLocal()
    try:
        if db.query(Question).count() > 0:
            print("Database already contains data. Skipping seed.")
            return

        for item in SAMPLE_DATA:
            question = Question(
                question_text=item["question_text"],
                category=item["category"],
            )
            db.add(question)
            db.flush()  # get question.id before adding choices

            for choice_text, is_correct in item["choices"]:
                db.add(
                    Choice(
                        choice_text=choice_text,
                        is_correct=is_correct,
                        question_id=question.id,
                    )
                )

        db.commit()
        print(f"Seeded {len(SAMPLE_DATA)} questions successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
