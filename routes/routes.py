# require all routes
from auth import auth
from test import test
from user import user

class Routes():
    ''' To keep readability and structure Flask uses blueprints '''
    ''' wire up the blueprints to keep each route in its own file '''
    def __init__(self, application):
        application.register_blueprint(test)
        application.register_blueprint(auth)
        application.register_blueprint(user)
