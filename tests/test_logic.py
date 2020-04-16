from app import create_app
from app.api.logic import get_available_langs_names, get_index


def test_available_langs_names() -> None:
    app = create_app('default')
    with app.app_context():
        available_langs_names = get_available_langs_names()
        assert isinstance(available_langs_names, list)


def test_index_full_match() -> None:
    app = create_app('default')
    with app.app_context():
        index = get_index({
            'target_lang': 'English',
            'known_langs': [{'English': 'Native'}]
        })
        assert index == 100


def test_index_no_match() -> None:
    app = create_app('default')
    with app.app_context():
        index = get_index({
            'target_lang': 'English',
            'known_langs': []
        })
        assert index == 0
