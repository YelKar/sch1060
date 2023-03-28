from flask import render_template

from app import app
from app.views import admin_panel, documents, \
    edit_documents, database, \
    files_include


@app.route('/')
def index():
    return render_template("index.html")
