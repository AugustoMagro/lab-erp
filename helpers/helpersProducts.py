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
    supplier = SelectField('Supplier')
    categoryPdv = SelectField('Category PDV')
    inventoryAmount = IntegerField('Inventory Amount', [validators.DataRequired()])
    volume = IntegerField('Volume')
    weight = DecimalField('Weight', [validators.DataRequired()])
    unit = IntegerField('Unit')
    costBase = DecimalField('Base Cost', [validators.DataRequired()])
    costTransport = DecimalField('Transport Cost', [validators.DataRequired()])
    costFinal = DecimalField('Final Cost', [validators.DataRequired()])
    costPrice = DecimalField('Price', [validators.DataRequired()])
    save = SubmitField('Save')


class EditProductForm(FlaskForm):
    id = StringField('Id', [validators.DataRequired()])
    barcode = StringField('Barcode', [validators.DataRequired(), validators.Length(min=1, max=50)])
    ncm = StringField('NCM', [validators.DataRequired(), validators.Length(min=1, max=50)])
    name = StringField('Name', [validators.DataRequired(), validators.Email()])
    description = StringField('Description', [validators.DataRequired()])
    supplier = StringField('Supplier', [validators.DataRequired()])
    categoryPdv = StringField('Category PDV', [validators.DataRequired()])
    inventoryAmount = IntegerField('Inventory Ammount', [validators.DataRequired()])
    volume = IntegerField('Volume')
    weight = DecimalField('Weight', [validators.DataRequired()])
    unit = IntegerField('Unit')
    costBase = DecimalField('Base Cost', [validators.DataRequired()])
    costTransport = DecimalField('Transport Cost', [validators.DataRequired()])
    costFinal = DecimalField('Final Cost', [validators.DataRequired()])
    costPrice = DecimalField('Price', [validators.DataRequired()])
    save = SubmitField('Save')

class NewCategoryPdv(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    save = SubmitField('Save')