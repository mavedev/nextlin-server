from flask import jsonify

from . import api
from ..model import db, Language


@api.route('/langs/<int:how_many>')
def get_posts(how_many: int) -> str:
    return jsonify(results=[
        lang.to_json() for lang in
        db.session.query(Language).limit(how_many).all()
    ])
