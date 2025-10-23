from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, services, database

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return services.user_service.create_user(db, user)

@router.get("/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return services.user_service.get_users(db, skip, limit)
