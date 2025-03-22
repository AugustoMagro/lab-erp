from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SelectField, SubmitField, IntegerField, DateField

class NewCustomerForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    lastName = StringField('Last name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    email = EmailField('E-mail', [validators.DataRequired(), validators.Email()])
    number = IntegerField('Number', [validators.DataRequired()])
    birthdayDate = DateField('Birthday Date', [validators.DataRequired()])
    save = SubmitField('Save')

class EditCustomerForm(FlaskForm):
    id = StringField('Id', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    lastName = StringField('Last name', [validators.DataRequired(), validators.Length(min=1, max=50)])
    email = EmailField('E-mail', [validators.DataRequired(), validators.Email()])
    number = IntegerField('Number', [validators.DataRequired()])
    birthdayDate = DateField('Birthday Date', [validators.DataRequired()])
    save = SubmitField('Save')