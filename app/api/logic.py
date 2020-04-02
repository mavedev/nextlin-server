from typing import List, Dict, Tuple, Optional

from app.constants import JSONLike
from app.model import db, Language

_LangData = List[Tuple[str, str]]
_Languages = List[Language]
_levels = {
    'no_lvl': 0.0,
    'novice': 0.2,
    'middle': 0.4,
    'strong': 0.6,
    'master': 0.8,
    'native': 1.0,
}


class LangLevelInfo:
    """Class representing language and its scale coefficient
       (according to given values).
    """

    def __init__(self, language: Language, scale: float) -> None:
        if any([
            language is None,
            scale is None
        ]):
            raise ValueError('LangLevelInfo invalid init args.')
        self._language = language
        self._scale = scale

    @property
    def language(self) -> Language:
        return self._language

    @property
    def scale(self) -> float:
        return self._scale


def get_available_langs_names() -> List[str]:
    return [
        lang.name for lang in
        db.session.query(Language).all()
    ]


def get_index(request: JSONLike) -> int:
    """Get the index value."""
    target_lang = _get_lang_from_db(request['target_lang'])

    scale = _get_scale(request, target_lang)
    match = _get_match(request, target_lang)
    index = _get_index(scale, match)

    return index


def _get_scale(request: JSONLike, target_lang: Language) -> float:
    """Get a scale coefficient."""
    given_langs = _get_given_langs_info(request)
    langs_infos = _get_wrapped_langs_info(given_langs)
    close_langs = _get_close_langs(langs_infos, target_lang)

    return 0.0 if not close_langs else sorted(
        close_langs,
        key=lambda linfo: linfo.scale,
        reverse=True
    )[0].scale


def _get_match(request: JSONLike, target: Language) -> Dict[str, bool]:
    """Get matches of all of the comparing languages' parameters."""
    native = _get_lang_from_db(request['native'])
    n_family, n_group = Language.get_split_origin(native.origin)
    t_family, t_group = Language.get_split_origin(target.origin)
    return {
        'family': t_family == n_family,
        'group': t_group == n_group,
        'has_articles': target.has_articles == native.has_articles,
        'mrph_alignment': target.mrph_alignment == native.mrph_alignment,
        'dominant_order': target.dominant_order == native.dominant_order,
        'writing_system': target.writing_system == native.writing_system,
        'genders': target.genders == native.genders,
        'cases': target.cases == native.cases,
        'ct_range': target.ct_range == native.ct_range
    }


def _get_index(scale: float, match: Dict[str, bool]) -> int:
    """Get the succes index for given dictionary of matches."""
    params: int = len(match)
    price: float = 100 / params
    weighted_price: float = price * scale
    return round(sum([
        weighted_price * param_match
        for param_match in match.values() if param_match
    ])) if any(match.values()) else 0


def _get_lang_from_db(lang_name: str) -> Optional[Language]:
    """Get a Language object from the database."""
    return (
        db.session.query(Language)
        .filter(Language.name == lang_name)
        .first()
    )


def _get_given_langs_info(request: JSONLike) -> _LangData:
    """Get Tuples containing languages names and levels
       (according to the request).
    """
    result = [
        (lang, level)
        for langinfo in request['known_langs']
        for lang, level in langinfo.items()  # type: ignore
    ]
    result.append((request['native'], 'native'))
    return result


def _get_wrapped_langs_info(given_langs: _LangData) -> List[LangLevelInfo]:
    """Get tuples containing languages names and levels
       and get them wrapped into LangLevelInfo objects.
    """
    return [
        LangLevelInfo(
            _get_lang_from_db(lang),
            _get_scale_from_level(level)
        )
        for lang, level in given_langs
    ]


def _get_scale_from_level(level: str) -> float:
    """Get scale coefficient according to the level
       (represented as a string).
       The level value must be one of [
        'no_lvl', 'novice', 'middle', 'strong', 'master', 'native'
       ]
    """
    if level.lower() not in _levels.keys():
        raise ValueError(
            'level must be one of {}'.format(list(_levels.keys()))
        )
    return _levels[level.lower()]


def _get_close_langs(given_langs, target):
    # Comment-like type annotation to avoid max line lenth warning.
    # type: (List[LangLevelInfo], Language) -> List[LangLevelInfo]
    """Get languages which have the same origin as the target."""
    return [
        linfo for linfo in given_langs
        if linfo.language.origin == target.origin
    ]
