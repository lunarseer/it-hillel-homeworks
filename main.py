from flask import Flask
import json
from os import path
from faker import Faker
import csv
import requests


app = Flask('homework_flask')

SPACE_URL = 'http://api.open-notify.org/astros.json'

@app.route('/')
def index():
    return 'sorry not needed here'


@app.route("/requirements")
def requirements():
    with open(path.join(path.dirname(__file__), 'requirements.txt')) as f:
        data = {}
        for line in f.readlines():
            package, version = line.rstrip().split('==')
            data.update({package: version})
        return json.dumps(data)


@app.route('/generate-users')
def generate_users():
    fake = Faker()
    data = {}

    def get_user_data():
        name = fake.name()
        return {name: '{}@mail.com'.format(name.lower().replace(' ', '_'))}

    for _ in range(0, 100):
        data.update(get_user_data())
    return json.dumps(data)


@app.route("/mean")
def mean():
    with open(path.join(path.dirname(__file__), 'hw.csv')) as csvf:
        data = csv.reader(csvf, delimiter=',',)
        data = list(data)[1:-1]                     #removing broken rows

        heigth = sum(float(row[1]) for row in data) / len(data)
        weigth = sum(float(row[2]) for row in data) / len(data)
        return json.dumps(
            {"avg_heigth": heigth,
            "avg_weigth": weigth,
            }
        )

@app.route("/space")
def space():
    data = requests.request(url=SPACE_URL, method="GET")
    return json.dumps({"number": str(data.json().get("number", 0))})