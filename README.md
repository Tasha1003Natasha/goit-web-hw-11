# goit-web-hw-11

Contacts REST API built with FastAPI, SQLAlchemy, PostgreSQL, and Alembic.

## Features

- Create, read, update, and delete contacts.
- Search contacts by name, surname, or email.
- Get contacts with birthdays in the next 7 days.
- PostgreSQL database connection.
- Alembic migrations.
- Swagger documentation.

## Technologies

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker Compose
- Pydantic

## Project Structure

```text
.
├── main.py
├── docker-compose.yml
├── alembic.ini
├── requirements.txt
├── migrations/
│   ├── env.py
│   └── versions/
└── src/
    ├── conf/
    │   └── config.py
    ├── database/
    │   └── db.py
    ├── entity/
    │   └── models.py
    ├── repository/
    │   └── contacts.py
    ├── routes/
    │   └── contacts.py
    └── schemas/
        └── contact.py
```

## Environment Variables

Create a `.env` file in the project root using `.env.example` as a template:

```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

When running PostgreSQL through Docker Compose, these variables are used by the `db` service.

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run PostgreSQL

Start the database container:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

## Migrations

Create a new migration after changing SQLAlchemy models:

```bash
alembic revision --autogenerate -m "create contacts table"
```

Apply migrations:

```bash
alembic upgrade head
```

Check current migration:

```bash
alembic current
```

## Run Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Application URLs:

```text
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Health Check

```http
GET /api/healthchecker
```

### Contacts

Get all contacts:

```http
GET /api/contacts/
```

Get contacts with pagination:

```http
GET /api/contacts/?limit=10&offset=0
```

Search contacts by name, surname, or email:

```http
GET /api/contacts/?query=ivan
GET /api/contacts/?query=petrenko
GET /api/contacts/?query=gmail.com
```

Get contacts with birthdays in the next 7 days:

```http
GET /api/contacts/birthdays
```

Get one contact by ID:

```http
GET /api/contacts/{contact_id}
```

Create a contact:

```http
POST /api/contacts/
```

Request body:

```json
{
  "name": "Ivan",
  "surname": "Petrenko",
  "email": "ivan@example.com",
  "phone": "+380501234567",
  "birthday": "1995-08-13",
  "info": "Friend from university"
}
```

The `info` field is optional:

```json
{
  "name": "Ivan",
  "surname": "Petrenko",
  "email": "ivan@example.com",
  "phone": "+380501234567",
  "birthday": "1995-08-13"
}
```

Update a contact:

```http
PUT /api/contacts/{contact_id}
```

Delete a contact:

```http
DELETE /api/contacts/{contact_id}
```

## Useful Commands

Stop Docker containers:

```bash
docker compose down
```



