
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getenv
import json

app = Flask('flask-sqalchemy')
DBFILE = getenv('SQLDBFILE')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(DBFILE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(80), unique=False)
    LastName = db.Column(db.String(80), unique=False)
    Email = db.Column(db.String(120), unique=False)

@app.route("/names")
def names():
    UniqueNames = []
    FirstNames = [x.FirstName for x in User.query.all()]
    for name in FirstNames:
        if name not in UniqueNames:
            UniqueNames.append(name)
    return json.dumps({"unique_names": len(UniqueNames)})

