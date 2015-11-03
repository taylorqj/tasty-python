from flask import Blueprint
from flask import jsonify

auth = Blueprint('auth', __name__)

@auth.route('/auth/signup')
def signup():
    ''' sign a user up '''

@auth.route('/auth/login')
def login():
    ''' logs a user in '''
