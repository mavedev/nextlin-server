from flask import jsonify, request

from . import api
from . import logic


@api.route('/langs/available', methods=['GET'])
def get_available_langs_names() -> str:
    return jsonify(results=logic.get_available_langs_names())


@api.route('/langs/analyse', methods=['POST'])
def get_index() -> str:
    index = '{}%'.format(logic.get_index(request.json))
    return jsonify({
        'success_index': index
    })
