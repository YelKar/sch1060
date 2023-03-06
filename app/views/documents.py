from datetime import date

from flask import render_template, request

from app import app
from app.database import Student
from app.util.constants import docs_path, result_docs_path
from app.util.tools import get_documents

from doc_generating import generate


docs = get_documents()


@app.route('/select_document')
def select_document():
    if request.form:
        print(request.form)
    return render_template("select_document.html", documents=docs)


@app.route('/select_students', methods=['GET', 'POST'])
def select_students():
    today = date.today()
    return render_template(
        "select_students.html",
        db=Student.query,
        current_year=today.year - (today.month < Student.year_start_month)
    )


@app.route('/generate_document', methods=['POST'])
def generate_document():
    ids = list(map(int, request.data.split(b",")))
    students = Student.query.filter(Student.id.in_(ids)).all()
    generate("Документ", docs_path, "Документ111.docx", result_docs_path, students=list(map(
        lambda student: student.__dict__, students
    )))
    return "OK"


print(list(filter(lambda x: "in" in x, dir(Student.id))))

@app.route('/generate_table')
def generate_table():
    pass
