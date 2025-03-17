from main import app, db
from flask import Flask, render_template, request, redirect, url_for, session, flash
from helpers import NewUserForm, EditUserForm, LoginUserForm
from model import *
from flask_bcrypt import generate_password_hash, check_password_hash

@app.route('/login')
def login():
    form = LoginUserForm()
    nextPage = request.args.get("next")
    # return render_template('home/home.html')
    return render_template('pages/users/login.html', form=form, nextPage=nextPage)

@app.route('/autenticate', methods=["POST",])
def autenticate():
    form = LoginUserForm(request.form)
    user = User.query.filter_by(email=form.email.data).first()
    password = check_password_hash(user.password, form.password.data)
    if password:
        session['userLoged'] = user.id
        flash(f"Login {user.name} success")
        return redirect(form.nextPage.data)
    else:
        flash(f"Login not successfull")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session['userLoged'] = None
    flash(f"Logout with success!")
    return redirect(url_for("login", next=url_for('home')))

@app.route('/')
def home():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('home')))
    
    return render_template('pages/home/home.html')

@app.route('/dashboard')
def dashboard():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('dashboard')))
    
    return render_template('pages/dashboard/dashboard.html')

@app.route('/products')
def products():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('products')))

    return render_template('pages/products/products.html')

@app.route('/sales')
def sales():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('sales')))

    return render_template('pages/sales/sales.html')

@app.route('/users')
def users():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('users')))

    listUsers = User.query.order_by(User.id)
    return render_template('pages/users/users.html', users=listUsers)

@app.route('/suppliers')
def suppliers():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('suppliers')))

    return render_template('pages/suppliers/suppliers.html')

@app.route('/costumers')
def costumers():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('costumers')))

    return render_template('pages/costumers/costumers.html')

@app.route('/newuser')
def newUser():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('newUser')))

    form = NewUserForm()
    return render_template('pages/users/newUser.html', form=form)

@app.route('/edit/<int:id>')
def editUser(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('editUser')))

    form = EditUserForm()
    user = User.query.filter_by(id=id).first()
    return render_template('pages/users/editUser.html', form=form, user=user)

@app.route('/updateUser', methods=["POST",])
def updateUser():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('updateUser')))

    form = EditUserForm(request.form)
    idUser = form.id.data
    user = User.query.filter_by(id=idUser).first()
    user.name = form.name.data
    user.lastName = form.lastName.data
    user.email = form.email.data
    user.position = form.position.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for("users"))

@app.route('/createuser', methods=["POST",])
def createUser():
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('createUser')))

    form = NewUserForm(request.form)
    newUser = User(name=form.name.data, lastName=form.lastName.data, email=form.email.data, position=form.position.data, password=generate_password_hash(form.password.data).decode("utf-8"))

    db.session.add(newUser)
    db.session.commit()

    return redirect(url_for("users"))

@app.route('/deleteuser/<int:id>')
def deleteUser(id):
    if 'userLoged' not in session or session['userLoged'] == None:
        flash(f"User not loged!")
        return redirect(url_for("login", next=url_for('deleteUser')))

    User.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("users"))