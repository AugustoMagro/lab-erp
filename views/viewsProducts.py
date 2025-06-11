from app import app, db
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from model import *
from flask_bcrypt import generate_password_hash, check_password_hash
from helpers.helpersProducts import NewProductForm, EditProductForm, NewCategoryPdv

@app.route('/products')
def products():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('products')))

    listProducts = Product.query.order_by(Product.id)
    return render_template('pages/products/products.html', products=listProducts)

@app.route('/newproduct')
def newProduct():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('newProduct')))

    form = NewProductForm()
    formCategory = NewCategoryPdv()
    form.supplier.choices = [(s.id, s.name) for s in Supplier.query.order_by(Supplier.id)]
    form.categoryPdv.choices = [(c.id, c.name) for c in CategoryPdv.query.order_by(CategoryPdv.id)]
    listCategory = CategoryPdv.query.order_by(CategoryPdv.id)

    return render_template('pages/products/newProduct.html', form=form, formCategory=formCategory, listCategory=listCategory)

@app.route('/editproduct/<int:id>')
def editProduct(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('editProduct')))

    form = EditProductForm()
    product = Product.query.filter_by(id=id).first()
    return render_template('pages/products/editProduct.html', form=form, product=product)

@app.route('/updateProduct', methods=["POST",])
def updateProduct():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('updateProduct')))

    form = EditProductForm(request.form)
    idProduct = form.id.data
    product = Product.query.filter_by(id=idProduct).first()
    product.barcode = form.barcode.data
    product.ncm = form.ncm.data
    product.name = form.name.data
    product.description = form.description.data
    product.costPrice = form.costPrice.data

    db.session.add(product)
    db.session.commit()

    return redirect(url_for("products"))

@app.route('/createproduct', methods=["POST",])
def createProduct():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('createProduct')))

    form = NewProductForm(request.form)
    newProduct = Product(barcode=form.barcode.data, 
                        ncm=form.ncm.data, 
                        name=form.name.data, 
                        description=form.description.data, 
                        costPrice=form.costPrice.data)

    db.session.add(newProduct)
    db.session.commit()

    return redirect(url_for("products"))

@app.route('/deleteproduct/<int:id>')
def deleteProduct(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('deleteProduct')))

    product = Product.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for("products"))