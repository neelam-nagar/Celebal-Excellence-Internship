# Quiz Backend Management API (FastAPI)

## 🌐 Live Demo

- 🚀 **Live Application:** https://celebal-excellence-internship.onrender.com
- 📖 **Swagger API Documentation:** https://celebal-excellence-internship.onrender.com/docs

A RESTful backend for creating and managing quiz questions and answer choices, built with **FastAPI**, **SQLAlchemy** (ORM), and **Pydantic** (validation).

This is a **General Quiz Management System** that supports questions from any category (General Knowledge, Programming, Mathematics, Data Science, Business Studies, Aptitude, etc.) using the optional `category` field.

---

## Features

- ✅ CRUD operations for Questions
- ✅ CRUD operations for Choices
- ✅ SQLAlchemy ORM with SQLite (supports PostgreSQL/MySQL)
- ✅ Pydantic request validation
- ✅ Admin authentication with hashed passwords
- ✅ Token-based authorization (24-hour expiry)
- ✅ Cascade delete (Question → Choices)
- ✅ Interactive Swagger API documentation
- ✅ Category-based filtering
- ✅ Pagination support
- ✅ Responsive frontend for playing and managing quizzes

---

## Project Structure

```text
quiz_backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── routers/
│       ├── questions.py
│       └── choices.py
├── frontend/
│   └── index.html
├── set_admin_password.py
├── seed_data.py
├── requirements.txt
└── README.md
```

---

## Database Design

### Question

| Column | Type |
|---------|------|
| id | Integer |
| question_text | String |
| category | String (Optional) |

### Choice

| Column | Type |
|---------|------|
| id | Integer |
| choice_text | String |
| is_correct | Boolean |
| question_id | Foreign Key |

**Relationship**

One Question → Many Choices

Deleting a question automatically deletes all of its choices.

---

## Admin Authentication

Anyone can **play** the quiz.

Only authenticated admins can:

- Create Questions
- Update Questions
- Delete Questions
- Create Choices
- Update Choices
- Delete Choices

Security Features

- Password stored using PBKDF2 hashing
- Password never stored in plain text
- Signed authentication token
- Token expires after 24 hours

---

## Installation

### 1. Create Virtual Environment

```bash
python -m venv venv
```

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Admin Password

```bash
python set_admin_password.py
```

### 4. Seed Sample Data (Optional)

```bash
python seed_data.py
```

### 5. Run Server

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Question Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/questions` | Create Question |
| GET | `/questions` | Get All Questions |
| GET | `/questions/{id}` | Get Question by ID |
| PUT | `/questions/{id}` | Update Question |
| DELETE | `/questions/{id}` | Delete Question |

Supports

- category filter
- skip
- limit

---

### Choice Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/choices` | Create Choice |
| GET | `/choices` | Get All Choices |
| GET | `/choices/{id}` | Get Choice |
| PUT | `/choices/{id}` | Update Choice |
| DELETE | `/choices/{id}` | Delete Choice |

---

## Example Requests

### Create Question

```bash
curl -X POST http://127.0.0.1:8000/questions \
-H "Content-Type: application/json" \
-d '{
"question_text":"What is the capital of France?",
"category":"General Knowledge"
}'
```

---

### Create Choice

```bash
curl -X POST http://127.0.0.1:8000/choices \
-H "Content-Type: application/json" \
-d '{
"choice_text":"Paris",
"is_correct":true,
"question_id":1
}'
```

---

### Get Question

```bash
curl http://127.0.0.1:8000/questions/1
```

---

## Switching Database

SQLite (Default)

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./quiz.db"
```

PostgreSQL

```python
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/quizdb"
```

MySQL

```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/quizdb"
```

---

## Frontend

A responsive frontend is included inside

```
frontend/index.html
```

Features

- Play Quiz
- Category Selection
- Score Calculation
- Admin Login
- Add Questions
- Edit Questions
- Delete Questions
- Manage Choices

Run

```bash
cd frontend
python -m http.server 5500
```

Open

```
http://127.0.0.1:5500
```

---

## Validation

Pydantic validates

- Empty question text
- Required fields
- Boolean values
- Integer IDs

before any database operation.

---

## Architecture

```
Routes
      ↓
CRUD Layer
      ↓
SQLAlchemy Models
      ↓
Database
```

---

## Future Improvements

- JWT Authentication
- User Accounts
- Quiz Timer
- Leaderboard
- Attempt History
- Analytics Dashboard
- AI-based Adaptive Quiz

---

## Testing

✔ Create Question

✔ Read Question

✔ Update Question

✔ Delete Question

✔ Create Choice

✔ Read Choice

✔ Update Choice

✔ Delete Choice

✔ Cascade Delete

✔ Admin Authentication

✔ Swagger Documentation

---

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn
- HTML
- CSS
- JavaScript

---

## Author

Developed as part of the **Celebal Technologies Excellence Internship**.
