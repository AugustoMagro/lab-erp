from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SelectField, SubmitField, IntegerField, DateField, DecimalField

listSales = []
total_price: float = 0

class SearchProductForm(FlaskForm):
    barcode = StringField('Barcode')
    name = StringField('Name')
    search = SubmitField('Search')

class SaleItem():
    def __init__(self, id, barcode, name, price):
        self.id = id
        self.barcode = barcode
        self.name = name
        self.price = price