from fastapi import FastAPI
from .database import engine, Base
from .routes import task_routes, user_routes

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Tracker API")

app.include_router(user_routes.router)
app.include_router(task_routes.router)
