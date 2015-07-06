import flask
import flask.ext.sqlalchemy
import flask.ext.restless

URI = open('data/db_uri.txt', 'r').read().rstrip()

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = URI
db = flask.ext.sqlalchemy.SQLAlchemy(app)


class MatchFilters(db.Model):
    __tablename__ = 'match_filters'
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'))
    filter_id = db.Column(db.Integer, db.ForeignKey('filters.id'))


class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    matches = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, )
    filters = db.relationship("Filter",
                              secondary='match_filters')


class Filter(db.Model):
    __tablename__ = 'filters'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)
    args = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)


db.create_all()
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Match, methods=['GET'])
manager.create_api(Filter, methods=['GET', 'POST', 'DELETE'])

app.run()
