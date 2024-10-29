from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class AuditLog(Base):
    __tablename__ = "audit_logs"

#estos son las cosas que podemos ir viendo  que se fue modificando
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    action = Column(String, nullable=False)
    entity = Column(String, nullable=False)
    entity_id = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    details = Column(String, nullable=True)

    def __repr__(self):
        return f"<AuditLog(id={self.id}, user_id={self.user_id}, action='{self.action}', entity='{self.entity}', entity_id={self.entity_id}, timestamp={self.timestamp})>"
