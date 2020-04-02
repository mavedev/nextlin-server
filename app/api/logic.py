from typing import List, Optional

from app.constants import JSONLike
from app.model import db, Language

_levels = {
    'no_lvl': 0.0,
    'novice': 0.2,
    'middle': 0.4,
    'strong': 0.6,
    'master': 0.8,
    'native': 1.0,
}
_criteria_weights = {
    'family': 0.2,
    'group': 0.3,
    'has_articles': 0.05,
    'mrph_alignment': 0.07,
    'dominant_order': 0.05,
    'writing_system': 0.15,
    'genders': 0.1,
    'cases': 0.05,
    'ct_range': 0.03,
}


def get_available_langs_names() -> List[str]:
    return [
        lang.name for lang in
        db.session.query(Language).all()
    ]


def get_index(request: JSONLike) -> int:
    """Get the index value."""
    target_lang = _get_lang_from_db(request['target_lang'])
    known_langs = request['known_langs']

    if _contains_target(known_langs, target_lang):
        return 100

    return round(
        _get_resulted_similarity(known_langs, target_lang) * 100
    )


def _get_resulted_similarity(known_langs, target):
    # Comment-like type annotation to avoid max line lenth warning.
    # type: (List[JSONLike], Language) -> float
    results: List[float] = []
    langs_infos = [
        (lang, level)
        for langinfo in known_langs
        for lang, level in langinfo.items()
    ]
    for lang, level in langs_infos:
        dblang: Language = _get_lang_from_db(lang)
        if not dblang:
            continue
        results.append(_get_similarity(dblang, level, target))
    return max(results) if results else 0


def _get_similarity(known: Language, level: str, target: Language) -> float:
    results: List[float] = []
    for criteria, weight in _criteria_weights.items():
        results.append(
            int(getattr(known, criteria) == getattr(target, criteria))
            * weight
            * (_levels.get(level.lower()) or 0)
        )
    print(results, level, known.name)
    return sum(results)


def _get_lang_from_db(lang_name: str) -> Optional[Language]:
    """Get a Language object from the database."""
    return (
        db.session.query(Language)
        .filter(Language.name == lang_name)
        .first()
    )


def _contains_target(contains_where: JSONLike, target: Language) -> bool:
    for langinfo in contains_where:
        # Technically, proper langinfo always has one key-value pair.
        if target.name in langinfo:
            return True
    else:
        return False
