from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import json

app = Flask('flask-sqalchemy')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/test.db'.format(path.dirname(__file__))
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
    # return json.dumps({"unique_names": len(UniqueNames)})
    return json.dumps(sorted(UniqueNames))

