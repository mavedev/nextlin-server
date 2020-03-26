from flask import Flask


def get_app() -> Flask:
    app = Flask(__name__)
    return app
