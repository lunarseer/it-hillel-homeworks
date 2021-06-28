from os import path, remove, getenv
import csv

DBFILE = getenv('SQLDBFILE')

if path.exists(DBFILE):
    remove(DBFILE)

from app import db
from app import Sales


db.create_all()


def add_Sales():
    with open('homework3sales.csv', mode='r') as csvfile:
        csvdata = [x for x in csv.reader(csvfile[1:], delimiter=';')] #Removing first row with fields names
        for i, row in enumerate(csvdata):                       
            sale = Sales(Transaction_date=row[0],
                        Product=row[1],
                        Price=row[2],
                        Payment_Type=row[3]
                        )
            db.session.add(sale)
        db.session.commit()

if __name__ == '__main__':
    add_Sales()