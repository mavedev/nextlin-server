from flask_sqlalchemy import SQLAlchemy

from .constants import (
    _TEXT_SIZE_MAX,
    _TEXT_SIZE_MID,
    _TEXT_SIZE_MIN
)

db = SQLAlchemy()


class Origin(db.Model):  # type: ignore
    id = db.Column(db.Integer(), primary_key=True)
    full_origin = db.Column(db.String(_TEXT_SIZE_MAX), unique=True)
