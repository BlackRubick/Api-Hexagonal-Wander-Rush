class AuditRepository:
    @staticmethod
    def save(audit, db):
        db.add(audit)
        db.commit()
        db.refresh(audit)
