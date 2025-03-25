from main import app, db
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from model import *
from flask_bcrypt import generate_password_hash, check_password_hash
from helpers.helpersSales import SearchProductForm

@app.route('/sales')
def sales():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))

    form = SearchProductForm()
    listCustomers = Costumer.query.order_by(Costumer.id)
    return render_template('pages/sales/sales.html', form=form, listCustomers=listCustomers)

@app.route('/searchproduct', methods=['POST',])
def searchProduct():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))
    
    form = SearchProductForm()
    nameProduct = form.name.data
    barcodeProduct = form.barcode.data
    listCustomers = Costumer.query.order_by(Costumer.id)

    if barcodeProduct != "":
        products = Product.query.filter_by(barcode=barcodeProduct)
    elif nameProduct != "":
        products = Product.query.filter_by(name=nameProduct)

    return render_template('pages/sales/sales.html', form=form, listCustomers=listCustomers, products=products)