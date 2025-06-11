from app import app, db
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from model import *
from flask_bcrypt import generate_password_hash, check_password_hash
from helpers.helpersCustomers import NewCustomerForm, EditCustomerForm

@app.route('/costumers')
def costumers():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('costumers')))

    listCustomers = Costumer.query.order_by(Costumer.id)
    return render_template('pages/costumers/costumers.html', customers=listCustomers)

@app.route('/newCustomer')
def newCustomer():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('newCustomer')))

    form = NewCustomerForm()
    return render_template('pages/costumers/newCustomer.html', form=form)

@app.route('/editCustomer/<int:id>')
def editCustomer(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('editCustomer')))

    form = EditCustomerForm()
    customer = Costumer.query.filter_by(id=id).first()
    return render_template('pages/costumers/editCustomer.html', form=form, customer=customer)

@app.route('/updateCustomer', methods=["POST",])
def updateCustomer():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('updateCustomer')))

    form = EditCustomerForm(request.form)
    idCustomer = form.id.data
    customer = Costumer.query.filter_by(id=idCustomer).first()
    customer.name = form.name.data
    customer.lastName = form.lastName.data
    customer.email = form.email.data
    customer.number = form.number.data

    db.session.add(customer)
    db.session.commit()

    return redirect(url_for("costumers"))

@app.route('/createcustomer', methods=["POST",])
def createCustomer():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('createCustomer')))

    form = NewCustomerForm(request.form)
    newCustomer = Costumer(name=form.name.data, lastName=form.lastName.data, email=form.email.data, number=form.number.data, birthdayDate=form.birthdayDate.data)

    db.session.add(newCustomer)
    db.session.commit()

    return redirect(url_for("costumers"))

@app.route('/deletecustomer/<int:id>')
def deleteCustomer(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('deleteCustomer')))

    customer = Costumer.query.filter_by(id=id).first()
    db.session.delete(customer)
    db.session.commit()

    return redirect(url_for("costumers"))