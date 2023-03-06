from flask import render_template

from app import app

from app.views import admin_panel, documents


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/database')
def database():
    return render_template("index.html")
