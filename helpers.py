import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SelectField, SubmitField, IntegerField

class NewUserForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    lastName = StringField('Last name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    email = EmailField('E-mail', [validators.DataRequired(), validators.Email()])
    position = SelectField('Position', [validators.DataRequired()], choices=["Analyst", "Sales", "Manager"])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=5, max=20)])
    save = SubmitField('Save')

class EditUserForm(FlaskForm):
    id = StringField('Id', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    lastName = StringField('Last name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    email = EmailField('E-mail', [validators.DataRequired(), validators.Email()])
    position = SelectField('Position', [validators.DataRequired()], choices=["", "Analyst", "Sales", "Manager"])
    save = SubmitField('Save')

class LoginUserForm(FlaskForm):
    nextPage = StringField("Next Page", [validators.DataRequired()])
    email = EmailField('E-mail', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=5, max=20)])
    save = SubmitField('Login')