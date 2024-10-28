from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.schemas.user import UserCreate, UserOut
from core.services.user_service import create_user
from infrastructure.db.database import SessionLocal

router = APIRouter()

# Dependency para la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
