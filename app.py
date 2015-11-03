from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from routes.routes import Routes
from config import Config
from models.user import User

# instantiate our application with flask base
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config().db_uri

# wire up routes and blueprints from flask
Routes(app)

# wire up the db
db = SQLAlchemy(app)

# users = User.query.all()

if __name__ == '__main__':
    app.run(debug = True)
