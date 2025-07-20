# 🚂 KPA Form API (Wheel Specification)

This project implements Django REST API endpoints for submitting and retrieving **wheel specification forms**, as per the KPA backend assignment.

---

## ✅ Features

- `POST /api/forms/wheel-specifications/` — Submit wheel specification form
- `GET /api/forms/wheel-specifications/` — Retrieve wheel forms with optional filters
- PostgreSQL as database
- Swagger UI for API documentation

---

## 📦 Requirements

- Python 3.9+
- PostgreSQL 12+
- pip + venv (recommended)

---

## ⚙️ Setup Instructions

### 1. Clone or Download

Unzip the provided `assignment.zip` or clone the repo (if hosted on GitHub).

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:
```bash
pip install django djangorestframework psycopg2-binary drf-yasg
```

### 4. Set Up PostgreSQL Database

Ensure PostgreSQL is installed and running.

Create the database:
```sql
CREATE DATABASE kpa_db;
```

Ensure `settings.py` has correct credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kpa_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 Run the Server

```bash
python manage.py runserver
```

### 🔗 API Base: `http://localhost:8000/api/`

- `POST /forms/wheel-specifications/`  
- `GET /forms/wheel-specifications/?formNumber=...&submittedBy=...&submittedDate=...`

### 📚 Swagger Docs

- `http://localhost:8000/swagger/`

---

## 🧪 Postman Collection

Use the included `postman_collection.json` to test endpoints directly in Postman.

---

## 📁 Project Structure

```
kpa_project/
├── kpa_api/          # Django app (views, models, urls)
├── kpa_project/      # Project settings
├── manage.py
├── requirements.txt
├── README.md
├── postman_collection.json
```

---
