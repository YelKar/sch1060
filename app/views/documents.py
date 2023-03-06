from flask import render_template, request

from app import app
from app.util.tools import get_documents


docs = get_documents()


@app.route('/select_document')
def select_document():
    if request.form:
        print(request.form)
    return render_template("select_document.html", documents=docs)


@app.route('/select_students', methods=['GET', 'POST'])
def select_students():
    pass


@app.route('/generate_table')
def generate_table():
    pass
