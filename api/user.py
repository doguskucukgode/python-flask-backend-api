from flask import Blueprint

users_api = Blueprint('users_api', __name__, url_prefix='/users')


@users_api.route('/')
def index():
    return "users"
