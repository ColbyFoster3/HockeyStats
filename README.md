# Welcome to HockeyStats

This is a Python FastAPI & Uvicorn project to build a Hockey Stats tracker. This is a work in progess!

## Getting Started

1. Activate the virtual environment:
    Windows:

    ```text
    venv\Scripts\activate
    ```

    Mac:

    ```text
    source venv/bin/activate
    ```

2. Install packages:

    ```text
    pip install -r requirements.txt
    ```

3. Run migrations:

    Windows:

    ```text
    venv\Scripts\python -m alembic upgrade head
    ```

    Mac:

    ```text
    python -m alembic upgrade head

    ```

4. Start the server:

    ```text
    uvicorn app.main:app --reload
    ```

    Or

    ```text
    python -m app
    ```

    Or

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

### Seeding

The database can be seeded in development by running the following:

```text
python seed_db.py
```

### Create new venv

```text
python -m venv venv
```

## Open Swagger UI

- <http://127.0.0.1:8000/docs>
- <http://127.0.0.1:8000/redoc>
