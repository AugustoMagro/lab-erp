from app import app, db
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from model import *
from flask_bcrypt import generate_password_hash, check_password_hash
from helpers.helpersSuppliers import NewSupplierForm, EditSupplierForm

@app.route('/suppliers')
def suppliers():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('suppliers')))

    listSuppliers = Supplier.query.order_by(Supplier.id)
    return render_template('pages/suppliers/suppliers.html', suppliers=listSuppliers)

@app.route('/newsupplier')
def newSupplier():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('newSupplier')))

    form = NewSupplierForm()
    return render_template('pages/suppliers/newSupplier.html', form=form)

@app.route('/editsupplier/<int:id>')
def editSupplier(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('editSupplier')))

    form = EditSupplierForm()
    supplier = Supplier.query.filter_by(id=id).first()
    return render_template('pages/suppliers/editSupplier.html', form=form, supplier=supplier)

@app.route('/updateSupplier', methods=["POST",])
def updateSupplier():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('updateSupplier')))

    form = EditSupplierForm(request.form)
    idSupplier = form.id.data
    supplier = Supplier.query.filter_by(id=idSupplier).first()
    supplier.name = form.name.data
    supplier.lastName = form.lastName.data
    supplier.email = form.email.data
    supplier.number = form.number.data

    db.session.add(supplier)
    db.session.commit()

    return redirect(url_for("suppliers"))

@app.route('/createsupplier', methods=["POST",])
def createSupplier():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('createSupplier')))

    form = NewSupplierForm(request.form)
    newSupplier = Supplier(name=form.name.data, lastName=form.lastName.data, email=form.email.data, number=form.number.data)

    db.session.add(newSupplier)
    db.session.commit()

    return redirect(url_for("suppliers"))

@app.route('/deletesupplier/<int:id>')
def deleteSupplier(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('deleteSupplier')))

    supplier = Supplier.query.filter_by(id=id).first()
    db.session.delete(supplier)
    db.session.commit()

    return redirect(url_for("suppliers"))