from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, services, database

router = APIRouter()

# -------------------- USER ROUTES -------------------- #


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return services.user_service.create_user(db, user)


@router.get("/users", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return services.user_service.get_users(db, skip, limit)


@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = services.user_service.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int, user: schemas.UserCreate, db: Session = Depends(database.get_db)
):
    db_user = services.user_service.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = services.user_service.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


# -------------------- TASK ROUTES -------------------- #


@router.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    return services.task_service.create_task(db, task)


@router.get("/tasks", response_model=list[schemas.Task])
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return db.query(services.models.Task).offset(skip).limit(limit).all()


@router.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = services.task_service.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int, task: schemas.TaskCreate, db: Session = Depends(database.get_db)
):
    db_task = services.task_service.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed
    db.commit()
    db.refresh(db_task)
    return db_task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = services.task_service.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}


# -------------------- ASSIGN/UNASSIGN USERS -------------------- #


@router.post("/tasks/{task_id}/assign/{user_id}", response_model=schemas.Task)
def assign_user(task_id: int, user_id: int, db: Session = Depends(database.get_db)):
    return services.task_service.assign_user(db, task_id, user_id)


@router.post("/tasks/{task_id}/unassign/{user_id}", response_model=schemas.Task)
def unassign_user(task_id: int, user_id: int, db: Session = Depends(database.get_db)):
    return services.task_service.unassign_user(db, task_id, user_id)
