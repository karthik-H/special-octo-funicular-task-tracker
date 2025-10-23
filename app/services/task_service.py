from sqlalchemy.orm import Session
from .. import models, schemas

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def assign_user(db: Session, task_id: int, user_id: int):
    task = get_task(db, task_id)
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user not in task.assigned_users:
        task.assigned_users.append(user)
        db.commit()
        db.refresh(task)
    return task

def unassign_user(db: Session, task_id: int, user_id: int):
    task = get_task(db, task_id)
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user in task.assigned_users:
        task.assigned_users.remove(user)
        db.commit()
        db.refresh(task)
    return task
