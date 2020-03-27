from typing import Dict
from enum import Enum

from app.constants import JSONLike


class LangLevel(Enum):
    NO_LEVEL, BASIC, MIDDLE, STRONG, ADVANCED, NATIVE = range(6)


def get_index(request: JSONLike) -> int:
    scale = _get_scale(request)
    match = _get_match(request)
    index = _get_index(scale, match)
    return index


def _get_scale(request: JSONLike) -> float:
    pass


def _get_match(request: JSONLike) -> Dict[str, bool]:
    pass


def _get_index(scale: float, match: Dict[str, bool]) -> int:
    pass
