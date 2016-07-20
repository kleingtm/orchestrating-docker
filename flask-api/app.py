from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from users import user, users

print(' * HELLO UWSGI!!! * ')

# configure flask app, rest api, and mongodb (pymongo)
app = Flask(__name__)
api = Api(app)
mongo = PyMongo(app)

app.register_blueprint(user)  # register route from user.py
app.register_blueprint(users)  # register route from users.py


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# The below doesn't work! You must run the app outside of the __name__ == '__main__' block
if __name__ == '__main__':
    print(' ')
    print(' * uWSGI running on :5000/api/user')
    print(' * uWSGI running on :5000/api/users')
    print(' ')
    app.run()
