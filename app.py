from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# require routes todo: throw into req dir
from routes.test import test
from routes.auth import auth
from routes.user import user

# instantiate our application with flask base
app = Flask(__name__)

# setup config
app.config['SQLALCHEMY_DATABASE_URI'] = 'test'

# wire up the db
db = SQLAlchemy(app)

# require models

# register route blueprints todo: throw into register all func
app.register_blueprint(test)
app.register_blueprint(auth)
app.register_blueprint(user)

if __name__ == '__main__':
    app.run(debug = True)
