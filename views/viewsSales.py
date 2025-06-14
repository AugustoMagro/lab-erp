from app import app, db
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, send_file
from model import *
from flask_bcrypt import generate_password_hash, check_password_hash
from helpers.helpersSales import SearchProductForm, AddProductForm, listSales, SaleItem, total_price, go

@app.route('/sales')
def sales():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))

    form = SearchProductForm()
    formAdd = AddProductForm()
    listCustomers = Costumer.query.order_by(Costumer.id)
    total = 0
    for sale in listSales:
        total += sale.price

    return render_template('pages/sales/sales.html', form=form, formAdd=formAdd, listCustomers=listCustomers, 
    listSales=listSales, total=total)

@app.route('/searchproduct', methods=['POST',])
def searchProduct():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))
    
    form = SearchProductForm()
    formAdd = AddProductForm()
    nameProduct = form.name.data
    barcodeProduct = form.barcode.data
    listCustomers = Costumer.query.order_by(Costumer.id)

    if barcodeProduct != "":
        products = Product.query.filter_by(barcode=barcodeProduct)
    elif nameProduct != "":
        products = Product.query.filter(Product.name.ilike(f"%{nameProduct}%")).all()

    return render_template('pages/sales/sales.html', form=form, formAdd=formAdd, listCustomers=listCustomers, products=products, listSales=listSales, total=0)

@app.route('/addsale/<int:id>', methods=['POST',])
def addSale(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))
    
    form = SearchProductForm()
    listCustomers = Costumer.query.order_by(Costumer.id)

    formAdd = AddProductForm()
    amount = formAdd.amount.data

    item = Product.query.filter_by(id=id).first()
    listSales.append(SaleItem(amount, item.id, item.barcode, item.name, item.costPrice, item.costPrice*amount))

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
            return redirect(url_for("sales"))

    return redirect(url_for("sales"))

@app.route('/confirmsale')
def confirmSale():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))
    
    total = sum([sale.price for sale in listSales])

    newSale = Sale(idCostumer=1, 
                        discount=0, 
                        salePrice=total,
                        paymentMethod="Credit")

    db.session.add(newSale)
    db.session.commit()

    for sale in listSales:
        idProduct = sale.id
        product = Product.query.filter_by(id=idProduct).first()
        
        product.storage = product.storage - sale.amount

        db.session.add(product)

    db.session.commit()

    pdf_file = go()

    listSales.clear()

    return send_file(pdf_file, as_attachment=True, download_name='venda.pdf')
