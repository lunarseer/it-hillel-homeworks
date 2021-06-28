
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from os import path, getenv

import re
import math

app = Flask('flask-sqalchemy')
DBFILE = getenv('SQLDBFILE')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}'.format(DBFILE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Transaction_date = db.Column(db.String(80), unique=False)
    Product = db.Column(db.String(80), unique=False)
    Price = db.Column(db.String(120), unique=False)
    Payment_Type = db.Column(db.String(40), unique=False)

@app.route("/summary")
def summary():
    sales = Sales.query.all()[1:]
    sale_days = []
    day_summary = {}
    for sale in sales:
        sale_day = sale.Transaction_date.split()[0]
        if not sale_day in sale_days:
            sale_days.append(sale_day)
    for day in sale_days:
        day_sales = list(filter(lambda x: re.search(day, x.Transaction_date), sales))
        day_summary[day] = sum([float(x.Price) for x in day_sales])
    return day_summary

@app.route('/sales')
def sales():
    product = request.args.get('product')
    payment_type = request.args.get('payment_type')
    sales = Sales.query.all()

    result = {}

    def sale_to_list(sale):
        return [
            sale.Transaction_date,
            sale.Product,
            sale.Price,
            sale.Payment_Type]
        
    filtered = sales
    if product:
        filtered = list(filter(lambda x: product==x.Product, filtered))
    if payment_type:
        filtered = list(filter(lambda x: payment_type==x.Payment_Type, filtered))

    
    result = {sale.id: sale_to_list(sale) for sale in filtered}
            
    return result