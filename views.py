from app import app
from flask import Flask, render_template, request, redirect, url_for
from helpers import NewUserForm

listaUsers = []

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
    return render_template('pages/users/users.html', users=listaUsers)

@app.route('/suppliers')
def suppliers():
    return render_template('pages/suppliers/suppliers.html')

@app.route('/costumers')
def costumers():
    return render_template('pages/costumers/costumers.html')

@app.route('/newuser')
def newUser():
    form = NewUserForm()
    return render_template('pages/users/newUser.html', form=form)

@app.route('/createuser', methods=["POST",])
def createUser():
    form = NewUserForm(request.form)
    return redirect(url_for("users"))