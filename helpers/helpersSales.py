from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SelectField, SubmitField, IntegerField, DateField, DecimalField

class SearchProductForm(FlaskForm):
    barcode = StringField('Barcode')
    name = StringField('Name')
    search = SubmitField('Search')