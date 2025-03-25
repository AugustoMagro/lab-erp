from main import app, db
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from model import *
from flask_bcrypt import generate_password_hash, check_password_hash

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