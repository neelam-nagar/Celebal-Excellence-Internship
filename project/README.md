# 🎯 Quiz Backend Management API (FastAPI)

<p align="center">

<img src="https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Pydantic-Validation-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite"/>

</p>

<p align="center">

<a href="https://celebal-excellence-internship.onrender.com">
<img src="https://img.shields.io/badge/🚀%20Live%20Demo-Open%20Application-success?style=for-the-badge"/>
</a>

<a href="https://celebal-excellence-internship.onrender.com/docs">
<img src="https://img.shields.io/badge/📖%20Swagger%20Docs-Explore%20API-blue?style=for-the-badge"/>
</a>

</p>

---

## 📌 Overview

A **RESTful Quiz Backend Management System** built using **FastAPI**, **SQLAlchemy**, and **Pydantic**.

The application provides secure CRUD operations for quiz questions and answer choices while supporting multiple quiz categories such as:

- 📚 General Knowledge
- 💻 Programming
- ➗ Mathematics
- 🤖 Data Science
- 💼 Business Studies
- 🧠 Aptitude
- and many more...

The backend also includes **Admin Authentication**, **Token-based Authorization**, **Swagger Documentation**, and a responsive **Quiz Frontend**.

---

# ✨ Features

- ✅ Create, Read, Update & Delete Questions
- ✅ Create, Read, Update & Delete Choices
- ✅ Category-wise Quiz Management
- ✅ Secure Admin Login
- ✅ Password Hashing (PBKDF2)
- ✅ Signed Authentication Tokens
- ✅ Token Expiration (24 Hours)
- ✅ SQLAlchemy ORM
- ✅ SQLite Database
- ✅ Supports PostgreSQL & MySQL
- ✅ Cascade Delete
- ✅ Request Validation using Pydantic
- ✅ Pagination Support
- ✅ Interactive Swagger Documentation
- ✅ Responsive Frontend
- ✅ Clean Project Structure

---

# 🖥️ Live Demo

| Service | Link |
|---------|------|
| 🚀 Live Application | https://celebal-excellence-internship.onrender.com |
| 📖 Swagger API Docs | https://celebal-excellence-internship.onrender.com/docs |

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API Framework |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| SQLite | Default Database |
| PostgreSQL | Optional Database |
| MySQL | Optional Database |
| Uvicorn | ASGI Server |
| HTML | Frontend |
| CSS | Styling |
| JavaScript | Frontend Logic |

---

# 📁 Project Structure

```text
quiz_backend/
│
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
│
├── frontend/
│   └── index.html
│
├── seed_data.py
├── set_admin_password.py
├── requirements.txt
└── README.md
```

---

# 🗄️ Database Design

## Question

| Field | Type |
|------|------|
| id | Integer |
| question_text | String |
| category | String (Optional) |

## Choice

| Field | Type |
|------|------|
| id | Integer |
| choice_text | String |
| is_correct | Boolean |
| question_id | Foreign Key |

### Relationship

```
Question
   │
   ├── Choice
   ├── Choice
   ├── Choice
```

Deleting a Question automatically deletes all associated Choices.

---

# 🔐 Authentication

Anyone can **play the quiz**.

Only Admins can

- Add Questions
- Edit Questions
- Delete Questions
- Add Choices
- Update Choices
- Delete Choices

Security Features

- 🔒 PBKDF2 Password Hashing
- 🔒 Signed Authentication Token
- 🔒 Token Expiration (24 Hours)
- 🔒 Unauthorized Access Protection

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/neelam-nagar/Celebal-Excellence-Internship.git

cd Celebal-Excellence-Internship/project
```

---

## Create Virtual Environment

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

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Set Admin Password

```bash
python set_admin_password.py
```

---

## Seed Sample Data

```bash
python seed_data.py
```

---

## Run Server

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

# 🌐 Frontend

The project includes a fully functional frontend located at

```
frontend/index.html
```

Features

- 🎮 Play Quiz
- 📂 Category Selection
- 📝 Manage Questions
- ➕ Add Questions
- ✏️ Edit Questions
- ❌ Delete Questions
- 📊 Score Calculation

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

# 📡 API Endpoints

## Questions

| Method | Endpoint |
|---------|----------|
| POST | /questions |
| GET | /questions |
| GET | /questions/{id} |
| PUT | /questions/{id} |
| DELETE | /questions/{id} |

Supports

- category
- skip
- limit

---

## Choices

| Method | Endpoint |
|---------|----------|
| POST | /choices |
| GET | /choices |
| GET | /choices/{id} |
| PUT | /choices/{id} |
| DELETE | /choices/{id} |

---

# 💻 Example API Request

Create Question

```bash
curl -X POST http://127.0.0.1:8000/questions \
-H "Content-Type: application/json" \
-d '{
"question_text":"What is the capital of France?",
"category":"General Knowledge"
}'
```

Create Choice

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

# 🔄 Switching Database

SQLite

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

# 🧪 Testing

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

# 🚀 Future Improvements

- JWT Authentication
- User Accounts
- Quiz Timer
- Leaderboard
- Quiz History
- Analytics Dashboard
- AI-based Quiz Recommendation
- Difficulty Levels

---

# 🏗️ Architecture

```
Client
   │
   ▼
FastAPI Routes
   │
   ▼
CRUD Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQLite / PostgreSQL / MySQL
```

---

# 👩‍💻 Author

**Neelam Nagar**

Developed as part of the **Celebal Technologies Excellence Internship**.

⭐ If you found this project useful, consider giving it a star on GitHub!
