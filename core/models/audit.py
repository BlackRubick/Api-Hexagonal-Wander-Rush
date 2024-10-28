from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # ID del usuario que realizó la acción
    action = Column(String, nullable=False)  # Descripción de la acción (ej. "Creación", "Edición", "Eliminación")
    entity = Column(String, nullable=False)  # Entidad afectada (ej. "Publicación", "Usuario")
    entity_id = Column(Integer, nullable=False)  # ID de la entidad afectada
    timestamp = Column(DateTime, default=datetime.utcnow)  # Fecha y hora de la acción
    details = Column(String, nullable=True)  # Detalles adicionales de la acción

    def __repr__(self):
        return f"<AuditLog(id={self.id}, user_id={self.user_id}, action='{self.action}', entity='{self.entity}', entity_id={self.entity_id}, timestamp={self.timestamp})>"
