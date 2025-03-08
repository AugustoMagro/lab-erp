from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('home/home.html')
    return render_template('home/home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')

app.run()