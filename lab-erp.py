from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('home/home.html')
    return render_template('pages/home/home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('pages/dashboard/dashboard.html')

@app.route('/products')
def products():
    return render_template('pages/products/products.html')

@app.route('/sales')
def sales():
    return render_template('pages/sales/sales.html')

@app.route('/users')
def users():
    return render_template('pages/users/users.html')

@app.route('/suppliers')
def suppliers():
    return render_template('pages/suppliers/suppliers.html')

@app.route('/costumers')
def costumers():
    return render_template('pages/costumers/costumers.html')

@app.route('/newuser')
def newUser():
    return render_template('pages/users/newUser.html')

app.run()