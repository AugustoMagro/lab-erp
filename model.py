from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return f'<User {self.name}>'
    
class Costumer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    number = db.Column(db.BigInteger, nullable=True)
    birthdayDate = db.Column(db.Date, nullable=True)
    
    def __repr__(self):
        return f'<Costumer {self.name}>'

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    number = db.Column(db.BigInteger, nullable=True)
    
    def __repr__(self):
        return f'<Supplier {self.name}>'
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.Integer, nullable=False)
    ncm = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    supplier = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    categoryPdv = db.Column(db.String(100), nullable=False)
    inventoryAmount = db.Column(db.Integer, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Double, nullable=False)
    unit = db.Column(db.Integer, nullable=False)
    costBase = db.Column(db.Double, nullable=False)
    costTransport = db.Column(db.Double, nullable=False)
    costFinal = db.Column(db.Double, nullable=False)
    costPrice = db.Column(db.Double, nullable=False)
    
    def __repr__(self):
        return f'<Product {self.name}>'
    
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProduct = db.Column(db.Integer, db.ForeignKey('product.id'))
    idCostumer = db.Column(db.Integer, nullable=True)
    discount = db.Column(db.Double, nullable=False)
    salePrice = db.Column(db.Double, nullable=False)
    paymentMethod = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<Sale {self.idProduct}>'