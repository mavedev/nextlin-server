from flask import jsonify, request

from . import api
from . import logic
from ..model import db, Language


@api.route('/langs/<int:how_many>')
def get_posts(how_many: int) -> str:
    return jsonify(results=[
        lang.to_json() for lang in
        db.session.query(Language).limit(how_many).all()
    ])


@api.route('/langs/analyse', methods=['POST'])
def get_index() -> str:
    logic.get_index(request.json)
    return jsonify({})
