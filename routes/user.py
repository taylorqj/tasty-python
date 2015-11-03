from flask import Blueprint
from flask import jsonify

user = Blueprint('user', __name__)

@user.route('/user')
def get_user():
    ''' do something to get the user '''

@user.route('/users')
def get_users():
    ''' do something to get the users '''

@user.route('/user/follow/<userId>')
def follow(userId):
    ''' do something to follow a user '''

@user.route('/user/unfollow/<userId>')
def unfollow(userId):
    ''' do something to unfollow a user '''
