from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=True)
    
    def __repr__(self):
        return f'<User {self.name}>'
    
class Costumer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    number = db.Column(db.Integer, nullable=True)
    birthdayDate = db.Column(db.Date, nullable=True)
    
    def __repr__(self):
        return f'<User {self.name}>'

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    number = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return f'<User {self.name}>'