from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, services, database

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    return services.task_service.create_task(db, task)

@router.get("/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = services.task_service.get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.post("/{task_id}/assign/{user_id}", response_model=schemas.Task)
def assign_user(task_id: int, user_id: int, db: Session = Depends(database.get_db)):
    return services.task_service.assign_user(db, task_id, user_id)

@router.post("/{task_id}/unassign/{user_id}", response_model=schemas.Task)
def unassign_user(task_id: int, user_id: int, db: Session = Depends(database.get_db)):
    return services.task_service.unassign_user(db, task_id, user_id)
