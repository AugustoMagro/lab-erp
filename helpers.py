import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SelectField, SubmitField

class NewUserForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    lastName = StringField('Last name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    email = EmailField('E-mail', [validators.DataRequired(), validators.Email()])
    position = SelectField('Position', [validators.DataRequired()], choices=["Analyst", "Sales", "Manager"])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=5, max=20)])
    save = SubmitField('Save')


class User():
    def __init__(self, idUser, name, lastName, email, position, password):
        self.id=idUser
        self.name=name
        self.lastName=lastName
        self.email=email
        self.position=position
        self.password=password