# Task Tracker API

This is a simple Task Tracker API built with FastAPI, SQLAlchemy, and SQLite.

## Features
- CRUD for Tasks and Users
- Assign/Unassign users to tasks
- No UI, API-only service

## Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the server:
```bash
uvicorn app.main:app --reload
```

3. Open API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
