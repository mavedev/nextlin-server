from flask_sqlalchemy import SQLAlchemy

from .constants import (
    JSONLike,
    _TEXT_SIZE_MAX,
    _TEXT_SIZE_MIN,
)

db = SQLAlchemy()


class CategoriesRange(db.Model):  # type: ignore
    id = db.Column(db.Integer(), primary_key=True)
    min_value = db.Column(db.Integer())
    max_value = db.Column(db.Integer())

    def serialize(self) -> JSONLike:
        return {
            'min': self.min_value,
            'max': self.max_value
        }


class Language(db.Model):  # type: ignore
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(_TEXT_SIZE_MIN), unique=True)
    has_articles = db.Column(db.Boolean(), default=False)
    mrph_alignment = db.Column(db.String(_TEXT_SIZE_MIN))
    dominant_order = db.Column(db.String(_TEXT_SIZE_MIN))
    writing_system = db.Column(db.String(_TEXT_SIZE_MIN))
    genders = db.Column(db.Integer())
    cases = db.Column(db.Integer())

    def serialize(self) -> JSONLike:
        return {
            'name': self.name,
            'has_articles': self.has_articles,
            'mrph_alignment': self.mrph_alignment,
            'dominant_order': self.dominant_order,
            'writing_system': self.writing_system,
            'genders': self.genders,
            'cases': self.cases
        }
