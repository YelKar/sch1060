import json
import os.path
from datetime import date, datetime

from docx2pdf import convert
from flask import render_template, request, url_for, send_file

from app import app
from app.database import Student
from app.util.logger import logger
from app.util.constants import docs_path, result_docs_path
from app.util.tools import get_documents

from doc_generating import generate


docs = tuple(".".join(doc.split(".")[:-1]) for doc in get_documents())


@app.route('/select_document')
def select_document():
    if request.form:
        print(request.form)
    return render_template("select_document.html", documents=docs)


@app.route('/select_students', methods=['GET', 'POST'])
def select_students():
    document = request.form.get("document")
    today = date.today()
    return render_template(
        "select_students.html",
        db=Student.query,
        current_year=today.year - (today.month < Student.year_start_month),
        document=document
    )


@app.route('/generate_document', methods=['POST'])
def generate_document():
    data = json.loads(request.data)
    ids = data.get("ids")
    document = data.get("document")
    if document == "None":
        return "Error"
    doc_type = data.get("type").lower()

    students = Student.query.filter(Student.id.in_(ids)).all()
    doc_name = datetime.now().strftime(f'{document}''__%d_%m_%Y__%H-%M-%S.%f.{type}')
    generate(
        document, docs_path,
        doc_name.format(type="docx"), result_docs_path,
        students=list(map(Student.to_dict, students))
    )
    if doc_type == "docx":
        return url_for("download_file", file=doc_name.format(type="docx"))
    # if doc_type == "pdf":
    #     convert(doc_path, os.path.join(result_docs_path, doc_name.format(type="pdf")))


@app.route('/download_file/<string:file>')
def download_file(file):
    logger.log("FILE SENDING", "")
    return send_file(os.path.join(result_docs_path[4:], file), as_attachment=True)


@app.route('/generate_table')
def configure_table():
    today = date.today()
    return render_template(
        "configure_table.html",
        db=Student.query,
        current_year=today.year - (today.month < Student.year_start_month)
    )


@app.route('/generate_table', methods=['POST'])
def generate_table():
    pass
