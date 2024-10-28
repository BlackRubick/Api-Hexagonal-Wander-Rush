from sqlalchemy.orm import Session
from core.models.audit import AuditLog
from datetime import datetime

class AuditService:
    @staticmethod
    def log_action(
        db: Session,
        user_id: int,
        action: str,
        entity: str,
        entity_id: int,
        details: str = None
    ):
        """Registra una acción en el registro de auditoría.

        Args:
            db (Session): Sesión de la base de datos.
            user_id (int): ID del usuario que realizó la acción.
            action (str): Tipo de acción (ej. "Creación", "Edición", "Eliminación").
            entity (str): Entidad afectada (ej. "Publicación", "Usuario").
            entity_id (int): ID de la entidad afectada.
            details (str, optional): Detalles adicionales sobre la acción.
        """
        audit_log = AuditLog(
            user_id=user_id,
            action=action,
            entity=entity,
            entity_id=entity_id,
            timestamp=datetime.utcnow(),
            details=details,
        )
        db.add(audit_log)
        db.commit()

    @staticmethod
    def get_audit_logs(db: Session, user_id: int = None):
        """Obtiene los registros de auditoría, filtrados opcionalmente por usuario.

        Args:
            db (Session): Sesión de la base de datos.
            user_id (int, optional): ID del usuario para filtrar los registros. Por defecto, None.

        Returns:
            List[AuditLog]: Lista de registros de auditoría.
        """
        query = db.query(AuditLog)
        if user_id:
            query = query.filter(AuditLog.user_id == user_id)
        return query.order_by(AuditLog.timestamp.desc()).all()
