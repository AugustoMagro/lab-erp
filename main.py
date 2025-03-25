from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from flask_s3 import FlaskS3
from flask_bcrypt import Bcrypt
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = str(os.getenv("SECRET_KEY"))
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# app.config['FLASKS3_BUCKET_NAME'] = os.getenv("FLASKS3_BUCKET_NAME")
# app.config['AWS_ACCESS_KEY_ID'] = os.getenv("AWS_ACCESS_KEY_ID")
# app.config['AWS_SECRET_ACCESS_KEY'] = os.getenv("AWS_SECRET_ACCESS_KEY")
# app.config['ACL'] = os.getenv("ACL")

# s3 = FlaskS3(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)


from views.views import *
from views.viewsUsers import *
from views.viewsCustomers import *
from views.viewsSuppliers import *
from views.viewsProducts import *
from views.viewsSales import *
from model import *

# Commit your model (table) to the database
if __name__ == '__main__':
    app.run(debug=True)