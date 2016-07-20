from flask import Blueprint
user = Blueprint('user', __name__)
users = Blueprint('users', __name__)


@user.route('/flask-api/user')
def user_fn():
    print(' * HELLO USER!!! * ')
    return "Hey single user!"


@users.route('/flask-api/users')
def users_fn():
    return "Hey multiple users!"
