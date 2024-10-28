from core.models.user import User
from core.schemas.user import UserCreate
from infrastructure.db.database import SessionLocal
from sqlalchemy.orm import Session

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
