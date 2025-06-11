from app import app, db
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from model import *
from flask_bcrypt import generate_password_hash, check_password_hash
from helpers.helpersSales import SearchProductForm, listSales, SaleItem, total_price

@app.route('/sales')
def sales():

    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))

    form = SearchProductForm()
    listCustomers = Costumer.query.order_by(Costumer.id)
    total = 0
    for sale in listSales:
        total += sale.price

    return render_template('pages/sales/sales.html', form=form, listCustomers=listCustomers, 
    listSales=listSales, total=total)

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
        products = Product.query.filter(Product.name.ilike(f"%{nameProduct}%")).all()

    return render_template('pages/sales/sales.html', form=form, listCustomers=listCustomers, products=products, listSales=listSales, total=0)

@app.route('/addsale/<int:id>')
def addSale(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))
    
    form = SearchProductForm()
    listCustomers = Costumer.query.order_by(Costumer.id)
    
    item = Product.query.filter_by(id=id).first()
    listSales.append(SaleItem(item.id, item.barcode, item.name, item.costPrice))

    # products = listSales

    # return render_template('pages/sales/sales.html', form=form, listCustomers=listCustomers, listSales=listSales, total=total_price)
    return redirect(url_for("sales"))

@app.route('/removesale/<int:id>')
def removeSale(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))
    
    form = SearchProductForm()
    listCustomers = Costumer.query.order_by(Costumer.id)
    
    item = Product.query.filter_by(id=id).first()
    
    for i in range(len(listSales)):
        idItem = listSales[i].id
        if idItem == id:
            listSales.pop(i)
            # return render_template('pages/sales/sales.html', form=form, listCustomers=listCustomers, listSales=listSales)
            return redirect(url_for("sales"))
    
    # return render_template('pages/sales/sales.html', form=form, listCustomers=listCustomers, listSales=listSales)
    return redirect(url_for("sales"))