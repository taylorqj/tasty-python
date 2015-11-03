from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from routes.routes import Routes

# instantiate our application with flask base
app = Flask(__name__)

# wire up routes and blueprints from flask
Routes(app)

# setup config
app.config['SQLALCHEMY_DATABASE_URI'] = 'test'

# wire up the db
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug = True)
