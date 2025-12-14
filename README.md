# Welcome to HockeyStats

This is a Python FastAPI & Uvicorn project to build a Hockey Stats tracker

## Getting Started

Activate virtual env:

```text
venv\Scripts\activate
```

Start the server:

```text
python -m app
```

Or this:

```text
venv\Scripts\python -m uvicorn app.main:app --reload
```

The server runs at:
<http://127.0.0.1:8000>

## Guide

### Creating DB Models

1. Create a SQLAlchemy model for the object you want in app/models
2. Create Pydantic schema in app/schemas. This is optional but helps with API
3. Import the model in alembic/env.py
4. Generate a new migration, run this in root:

    ```text
    venv\Scripts\python -m alembic revision --autogenerate -m "create players table"
    ```

5. Apply the migration:

    ```text
    venv\Scripts\python -m alembic upgrade head
    ```

6. Create file in app/services to contain the buisness logic
7. Create the route in app/api
8. Include the router in app/main.py

## Open Swagger UI

- <http://127.0.0.1:8000/docs>
- <http://127.0.0.1:8000/redoc>
