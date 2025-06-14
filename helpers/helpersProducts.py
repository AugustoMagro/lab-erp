from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SelectField, SubmitField, IntegerField, DateField, DecimalField

# suppliersQuery = Supplier.query.order_by(Supplier.id)
LISTSUPPLIERS = [2]
LISTPDV = ["No item"]
# for supplier in suppliersQuery:
#     LISTSUPPLIERS.append("{} - {}".format(supplier.id, supplier.name))

class NewProductForm(FlaskForm):
    barcode = StringField('Barcode', [validators.DataRequired(), validators.Length(min=1, max=50)])
    ncm = StringField('NCM', [validators.DataRequired(), validators.Length(min=1, max=50)])
    name = StringField('Name', [validators.DataRequired(), validators.Email()])
    description = StringField('Description', [validators.DataRequired()])
    storage = StringField('Storage', [validators.DataRequired()])
    costPrice = DecimalField('Price', [validators.DataRequired()])
    save = SubmitField('Save')


class EditProductForm(FlaskForm):
    id = StringField('Id', [validators.DataRequired()])
    barcode = StringField('Barcode', [validators.DataRequired(), validators.Length(min=1, max=50)])
    ncm = StringField('NCM', [validators.DataRequired(), validators.Length(min=1, max=50)])
    name = StringField('Name', [validators.DataRequired(), validators.Email()])
    storage = StringField('Storage', [validators.DataRequired()])
    description = StringField('Description', [validators.DataRequired()])
    costPrice = DecimalField('Price', [validators.DataRequired()])
    save = SubmitField('Save')

class NewCategoryPdv(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    save = SubmitField('Add category')