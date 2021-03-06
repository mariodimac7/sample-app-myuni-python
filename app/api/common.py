from flask import Blueprint, jsonify, request

common = Blueprint('common', __name__)


@common.before_app_request
def only_json():
    if request.method == 'POST' and not request.is_json:
        return jsonify({'error': 'Payload should be a json'}), 400
