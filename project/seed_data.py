"""
Populates the database with sample quiz questions across multiple
categories (General Knowledge, Programming, Mathematics, Data Science).
10 questions per category (40 total).

Run with:
    python seed_data.py
"""

from app.database import Base, SessionLocal, engine
from app.models import Choice, Question

Base.metadata.create_all(bind=engine)

SAMPLE_DATA = [
    # ---------------- General Knowledge (10) ----------------
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
        "question_text": "Who wrote the play 'Romeo and Juliet'?",
        "category": "General Knowledge",
        "choices": [
            ("Charles Dickens", False),
            ("William Shakespeare", True),
            ("Mark Twain", False),
            ("Leo Tolstoy", False),
        ],
    },
    {
        "question_text": "Which is the largest ocean on Earth?",
        "category": "General Knowledge",
        "choices": [
            ("Atlantic Ocean", False),
            ("Indian Ocean", False),
            ("Pacific Ocean", True),
            ("Arctic Ocean", False),
        ],
    },
    {
        "question_text": "What is the national currency of Japan?",
        "category": "General Knowledge",
        "choices": [
            ("Yuan", False),
            ("Won", False),
            ("Yen", True),
            ("Ringgit", False),
        ],
    },
    {
        "question_text": "Which gas do plants primarily absorb from the atmosphere for photosynthesis?",
        "category": "General Knowledge",
        "choices": [
            ("Oxygen", False),
            ("Carbon Dioxide", True),
            ("Nitrogen", False),
            ("Hydrogen", False),
        ],
    },
    {
        "question_text": "The Great Wall is located in which country?",
        "category": "General Knowledge",
        "choices": [
            ("India", False),
            ("China", True),
            ("Japan", False),
            ("Mongolia", False),
        ],
    },
    {
        "question_text": "How many continents are there on Earth?",
        "category": "General Knowledge",
        "choices": [
            ("5", False),
            ("6", False),
            ("7", True),
            ("8", False),
        ],
    },
    {
        "question_text": "Which organ in the human body is primarily responsible for pumping blood?",
        "category": "General Knowledge",
        "choices": [
            ("Lungs", False),
            ("Heart", True),
            ("Liver", False),
            ("Kidney", False),
        ],
    },
    {
        "question_text": "Who was the first person to walk on the Moon?",
        "category": "General Knowledge",
        "choices": [
            ("Buzz Aldrin", False),
            ("Yuri Gagarin", False),
            ("Neil Armstrong", True),
            ("Michael Collins", False),
        ],
    },
    # ---------------- Programming (10) ----------------
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
        "question_text": "Which HTTP method is typically used to update an existing resource?",
        "category": "Programming",
        "choices": [
            ("GET", False),
            ("POST", False),
            ("PUT", True),
            ("DELETE", False),
        ],
    },
    {
        "question_text": "In Git, which command is used to create a new branch?",
        "category": "Programming",
        "choices": [
            ("git branch <name>", True),
            ("git new <name>", False),
            ("git create <name>", False),
            ("git checkout-new <name>", False),
        ],
    },
    {
        "question_text": "Which data structure uses FIFO (First In, First Out) ordering?",
        "category": "Programming",
        "choices": [
            ("Stack", False),
            ("Queue", True),
            ("Tree", False),
            ("Graph", False),
        ],
    },
    {
        "question_text": "What does 'CSS' stand for?",
        "category": "Programming",
        "choices": [
            ("Cascading Style Sheets", True),
            ("Computer Style Syntax", False),
            ("Creative Styling System", False),
            ("Colorful Style Sheets", False),
        ],
    },
    {
        "question_text": "Which of the following is NOT a Python data type?",
        "category": "Programming",
        "choices": [
            ("list", False),
            ("dict", False),
            ("tuple", False),
            ("array", True),
        ],
    },
    {
        "question_text": "Which SQL clause is used to filter rows before grouping?",
        "category": "Programming",
        "choices": [
            ("HAVING", False),
            ("WHERE", True),
            ("GROUP BY", False),
            ("ORDER BY", False),
        ],
    },
    {
        "question_text": "What is the time complexity of accessing an element in an array by index?",
        "category": "Programming",
        "choices": [
            ("O(1)", True),
            ("O(n)", False),
            ("O(log n)", False),
            ("O(n^2)", False),
        ],
    },
    {
        "question_text": "Which framework is commonly used for building REST APIs in Python?",
        "category": "Programming",
        "choices": [
            ("FastAPI", True),
            ("React", False),
            ("Bootstrap", False),
            ("jQuery", False),
        ],
    },
    # ---------------- Mathematics (10) ----------------
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
        "question_text": "What is the square root of 144?",
        "category": "Mathematics",
        "choices": [
            ("10", False),
            ("11", False),
            ("12", True),
            ("14", False),
        ],
    },
    {
        "question_text": "What is the value of pi (π), rounded to two decimal places?",
        "category": "Mathematics",
        "choices": [
            ("3.14", True),
            ("3.41", False),
            ("2.14", False),
            ("3.12", False),
        ],
    },
    {
        "question_text": "What is 15% of 200?",
        "category": "Mathematics",
        "choices": [
            ("20", False),
            ("25", False),
            ("30", True),
            ("35", False),
        ],
    },
    {
        "question_text": "How many degrees are there in the sum of interior angles of a triangle?",
        "category": "Mathematics",
        "choices": [
            ("90", False),
            ("180", True),
            ("270", False),
            ("360", False),
        ],
    },
    {
        "question_text": "What is the next prime number after 7?",
        "category": "Mathematics",
        "choices": [
            ("9", False),
            ("10", False),
            ("11", True),
            ("13", False),
        ],
    },
    {
        "question_text": "What is the result of 2 raised to the power of 5 (2^5)?",
        "category": "Mathematics",
        "choices": [
            ("16", False),
            ("32", True),
            ("64", False),
            ("25", False),
        ],
    },
    {
        "question_text": "What is the least common multiple (LCM) of 4 and 6?",
        "category": "Mathematics",
        "choices": [
            ("10", False),
            ("12", True),
            ("18", False),
            ("24", False),
        ],
    },
    {
        "question_text": "In a right-angled triangle, what is the name of the side opposite the right angle?",
        "category": "Mathematics",
        "choices": [
            ("Adjacent", False),
            ("Opposite", False),
            ("Hypotenuse", True),
            ("Base", False),
        ],
    },
    {
        "question_text": "What is the value of 0! (zero factorial)?",
        "category": "Mathematics",
        "choices": [
            ("0", False),
            ("1", True),
            ("Undefined", False),
            ("-1", False),
        ],
    },
    # ---------------- Data Science (10) ----------------
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
    {
        "question_text": "Which metric measures the average squared difference between predicted and actual values?",
        "category": "Data Science",
        "choices": [
            ("Mean Absolute Error", False),
            ("Mean Squared Error", True),
            ("R-squared", False),
            ("Precision", False),
        ],
    },
    {
        "question_text": "Which Python library is widely used for numerical computing with arrays?",
        "category": "Data Science",
        "choices": [
            ("NumPy", True),
            ("Django", False),
            ("Seaborn", False),
            ("Selenium", False),
        ],
    },
    {
        "question_text": "What does 'EDA' stand for in the context of data science?",
        "category": "Data Science",
        "choices": [
            ("Exploratory Data Analysis", True),
            ("Extended Data Architecture", False),
            ("Estimated Data Accuracy", False),
            ("Effective Data Aggregation", False),
        ],
    },
    {
        "question_text": "Which type of machine learning uses labeled data for training?",
        "category": "Data Science",
        "choices": [
            ("Unsupervised learning", False),
            ("Supervised learning", True),
            ("Reinforcement learning", False),
            ("Semi-random learning", False),
        ],
    },
    {
        "question_text": "Which chart type is best suited for showing the distribution of a single numeric variable?",
        "category": "Data Science",
        "choices": [
            ("Pie chart", False),
            ("Histogram", True),
            ("Line chart", False),
            ("Scatter plot", False),
        ],
    },
    {
        "question_text": "What does 'overfitting' mean in machine learning?",
        "category": "Data Science",
        "choices": [
            ("The model performs well on training data but poorly on new data", True),
            ("The model performs poorly on both training and test data", False),
            ("The model trains too quickly", False),
            ("The model uses too little data", False),
        ],
    },
    {
        "question_text": "Which algorithm is commonly used for classification problems?",
        "category": "Data Science",
        "choices": [
            ("Linear Regression", False),
            ("Logistic Regression", True),
            ("K-Means Clustering", False),
            ("PCA", False),
        ],
    },
    {
        "question_text": "What is the term for reducing the number of input variables in a dataset?",
        "category": "Data Science",
        "choices": [
            ("Data augmentation", False),
            ("Dimensionality reduction", True),
            ("Data normalization", False),
            ("Feature duplication", False),
        ],
    },
    {
        "question_text": "Which value represents the middle point of a sorted dataset?",
        "category": "Data Science",
        "choices": [
            ("Mean", False),
            ("Mode", False),
            ("Median", True),
            ("Range", False),
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
