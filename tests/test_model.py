import random
import string

from app.model import Language


def get_random_string() -> str:
    return ''.join(
        random.choices(string.ascii_uppercase, k=10)
    )


def test_new_language() -> None:
    name = get_random_string(),
    origin = get_random_string(),
    has_articles = random.randint(0, 3) & 1,
    mrph_alignment = get_random_string(),
    dominant_order = get_random_string(),
    writing_system = get_random_string(),
    genders = random.randint(0, 5),
    cases = random.randint(0, 40)

    lang = Language(
        name=name,
        origin=origin,
        has_articles=has_articles,
        mrph_alignment=mrph_alignment,
        dominant_order=dominant_order,
        writing_system=writing_system,
        genders=genders,
        cases=cases
    )
    assert lang.name == name
    assert lang.origin == origin
    assert lang.has_articles == has_articles
    assert lang.mrph_alignment == mrph_alignment
    assert lang.dominant_order == dominant_order
    assert lang.writing_system == writing_system
    assert lang.genders == genders
    assert lang.cases == cases
