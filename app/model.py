from flask_sqlalchemy import SQLAlchemy

from .constants import (
    JSONLike,
    _TEXT_SIZE_MAX,
)

db = SQLAlchemy()


class Origin(db.Model):  # type: ignore
    id = db.Column(db.Integer(), primary_key=True)
    full_origin = db.Column(db.String(_TEXT_SIZE_MAX), unique=True)

    def serialize(self) -> JSONLike:
        return {
            'full_origin': self.full_origin
        }
