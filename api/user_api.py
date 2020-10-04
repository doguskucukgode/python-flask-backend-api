from flask import Blueprint, request, Response, jsonify

from model.user import User
from datetime import datetime

users_api = Blueprint('users_api', __name__, url_prefix='/users')


@users_api.route('/')
def index():
    return "users"


@users_api.route('/add', methods=['POST'])
def add_user():
    try:
        name: str = ''
        surname: str = ''
        birth_date: datetime = None
        hobbies = []

        req_data = request.get_json()
        if 'name' in req_data:
            name = req_data['name']
        if 'surname' in req_data:
            surname = req_data['surname']
        if 'birth_date' in req_data:
            birth_date = datetime.strptime(req_data['birth_date'], '%Y-%m-%d')
        if 'hobbies' in req_data:
            hobbies = req_data['hobbies']
        user = User(name=name,
                    surname=surname,
                    birth_date=birth_date,
                    hobbies=hobbies)
    except ValueError:
        return Response('"error": "Invalid date format, date format should be %Y-%m-%d"',
                        status=400, mimetype='application/json')

    return Response(user.to_json(), status=201, mimetype='application/json')
