from flask_sqlalchemy import SQLAlchemy

from .constants import (
    JSONLike,
    _TEXT_SIZE_MAX,
    _TEXT_SIZE_MIN,
)

db = SQLAlchemy()


class Origin(db.Model):  # type: ignore
    id = db.Column(db.Integer(), primary_key=True)
    full_origin = db.Column(db.String(_TEXT_SIZE_MAX), unique=True)

    def serialize(self) -> JSONLike:
        return {
            'full_origin': self.full_origin
        }


class WritingSystem(db.Model):  # type: ignore
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(_TEXT_SIZE_MIN), unique=True)

    def serialize(self) -> JSONLike:
        return {
            'name': self.name
        }
