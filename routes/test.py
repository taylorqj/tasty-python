from flask import Blueprint
from flask import jsonify

test = Blueprint('test', __name__)

@test.route('/ping')
def pong():
    ''' Ping the API to see if it's alive '''
    return jsonify({ "ping": "pong" })
