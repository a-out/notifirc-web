import flask
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless

from models import Base, Match, Filter

URI = open('data/db_uri.txt', 'r').read().rstrip()

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(app)


def init_db():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.commit()


init_db()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Match, methods=['GET'])
manager.create_api(Filter, methods=['GET', 'POST', 'DELETE'])

app.run()
