from database import db


class ExportHistory(db.Model):

    __tablename__ = "export_history"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    group_name = db.Column(
        db.String(255)
    )

    member_count = db.Column(
        db.Integer,
        default=0
    )

    filename = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
