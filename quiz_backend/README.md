# Quiz Backend Management API (FastAPI)

A RESTful backend for creating and managing quiz questions and answer
choices, built with **FastAPI**, **SQLAlchemy** (ORM), and **Pydantic**
(validation). This is a **General Quiz Management System** — it supports
questions from any category (General Knowledge, Programming, Mathematics,
Data Science, Business Studies, Aptitude, etc.) via the optional
`category` field.

## Project Structure

```
quiz_backend/
├── app/
│   ├── main.py          # FastAPI app, router registration
│   ├── database.py      # SQLAlchemy engine/session setup
│   ├── models.py        # ORM models: Question, Choice
│   ├── schemas.py        # Pydantic request/response schemas
│   ├── crud.py           # Business logic / DB operations
│   └── routers/
│       ├── questions.py  # /questions endpoints
│       └── choices.py    # /choices endpoints
├── seed_data.py           # Populates sample questions across categories
├── requirements.txt
└── README.md
```

## Database Design

**Question table:** `id`, `question_text`, `category` (optional)
**Choice table:** `id`, `choice_text`, `is_correct`, `question_id` (FK)

Relationship: one Question → many Choices (cascade delete — deleting a
question removes its choices too).

## Setup

```bash
# 1. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Seed sample data
python seed_data.py

# 4. Run the server
uvicorn app.main:app --reload
```

Then open **http://127.0.0.1:8000/docs** for interactive Swagger UI where
you can try every endpoint directly in the browser.

## Switching Databases

By default this uses SQLite (`quiz.db`, zero setup). To use MySQL or
PostgreSQL instead, edit `app/database.py`:

```python
# PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/quizdb"

# MySQL (requires: pip install pymysql)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/quizdb"
```

## API Endpoints

### Question Management
| Method | Endpoint | Description |
|---|---|---|
| POST | `/questions` | Create a new quiz question |
| GET | `/questions` | Get all questions (supports `?category=`, `?skip=`, `?limit=`) |
| GET | `/questions/{id}` | Get a specific question (with its choices) |
| PUT | `/questions/{id}` | Update a question |
| DELETE | `/questions/{id}` | Delete a question and its choices |

### Choice Management
| Method | Endpoint | Description |
|---|---|---|
| POST | `/choices` | Add a new answer choice |
| GET | `/choices` | Get all answer choices |
| GET | `/choices/{id}` | Get a specific choice |
| PUT | `/choices/{id}` | Update a choice |
| DELETE | `/choices/{id}` | Delete a choice |

## Example Requests

**Create a question:**
```bash
curl -X POST http://127.0.0.1:8000/questions \
  -H "Content-Type: application/json" \
  -d '{"question_text": "What is the capital of France?", "category": "General Knowledge"}'
```

**Add a choice to it (use the returned question id):**
```bash
curl -X POST http://127.0.0.1:8000/choices \
  -H "Content-Type: application/json" \
  -d '{"choice_text": "Paris", "is_correct": true, "question_id": 1}'
```

**Get a question with all its choices:**
```bash
curl http://127.0.0.1:8000/questions/1
```

## Notes on This Implementation

- **Validation**: Pydantic schemas enforce required fields (e.g.
  `question_text` cannot be empty) and correct types before anything
  touches the database.
- **Cascade delete**: Deleting a question automatically deletes its
  associated choices (`cascade="all, delete-orphan"` in `models.py`).
- **Layered architecture**: routes (`routers/`) → business logic
  (`crud.py`) → ORM models (`models.py`) → database (`database.py`),
  which mirrors the architecture diagram in the project spec.

## Possible Extensions (per project spec)

- User authentication and authorization
- Timer-based quizzes, scoring, and leaderboards
- Quiz attempt history and analytics dashboard
- Adaptive quizzes / recommendation systems (ML-based)

## Frontend

A complete, attractive frontend lives in `frontend/index.html` — a
single self-contained HTML file (no build step, no framework) with a
chalkboard-themed **Play** mode and a paper-themed **Manage Questions**
(admin/CRUD) mode.

- **Play mode**: pick a category, answer questions pulled live from
  the API, get hand-drawn chalk checkmark/cross feedback, see your
  score at the end.
- **Manage Questions mode**: add, edit, and delete questions and
  choices — a full UI over every CRUD endpoint.

### Running it

1. Start the backend first (CORS is already enabled in `app/main.py`):
   ```bash
   uvicorn app.main:app --reload
   ```
2. Serve the frontend (don't just double-click the file — serve it so
   `fetch()` works cleanly):
   ```bash
   cd frontend
   python3 -m http.server 5500
   ```
3. Open **http://127.0.0.1:5500** in your browser.

If your backend runs somewhere other than `http://127.0.0.1:8000`,
update the `API_BASE` constant near the top of the `<script>` block in
`frontend/index.html`.

## Tested

Every endpoint was verified end-to-end (create → read → update →
delete, including cascade delete of choices when a question is
removed) before delivery.
