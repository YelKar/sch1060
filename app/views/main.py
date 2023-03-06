import time

from flask import render_template

from app import app
from app.util.logger import logger


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/select_document')
def select_document():
    return render_template("select_document.html")


@app.route('/generate_table')
def generate_table():
    pass


@app.route('/database')
def database():
    return render_template("index.html")


from app.views import admin_panel
