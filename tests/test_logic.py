from app import create_app
from app.api.logic import get_available_langs_names


def test_available_langs_names() -> None:
    app = create_app('default')
    with app.app_context():
        available_langs_names = get_available_langs_names()
        assert isinstance(available_langs_names, list)
