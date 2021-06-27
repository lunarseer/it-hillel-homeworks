from os import path, remove, getenv

DBFILE = getenv('SQLDBFILE')

if path.exists(DBFILE):
    remove(DBFILE)

from app import db
from app import User
from faker import Faker

db.create_all()

def add_users():
    fake = Faker()
    for _ in range(0, 500):
        name = fake.name()
        firstname, lastname = name.split()[:2]
        user = User(FirstName=firstname,
                    LastName=lastname,
                    Email='{}@example.com'.format(name.lower().replace(' ', '_')))
        db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    add_users()