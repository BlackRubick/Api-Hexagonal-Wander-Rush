from core.models.user import User
from infrastructure.db.database import SessionLocal

def get_user(db: SessionLocal, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
