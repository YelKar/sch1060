from docx import Document
from flask import request, render_template
from werkzeug.datastructures import FileStorage

from app import app
from app.database import Student, db
from doc_generating.get_data import from_doc


@app.route('/database')
def database():
    return render_template("database/database.html")


@app.route('/delete_students', methods=["POST"])
def delete_students():
    *ids, = map(int, bytes(request.data).decode().split(","))
    Student.query.filter(Student.id.in_(ids)).delete()
    db.session.commit()
    return "OK"


@app.route('/add_student', methods=["POST"])
def add_student():
    print(request.data)
    user_id = ...


@app.route("/edit_student/<int:student_id>")
def edit_student(student_id):
    return render_template(
        "database/edit_student.html",
        student_id=student_id
    )


@app.route('/load_classroom', methods=['POST'])
def load_classroom():
    file = request.files["file"]
    print(request.form)
    file.stream.seekable = lambda: True
    print(*from_doc(file.stream, "//фамилия// //имя// //отчество//"), sep="\n")
    return "OK"


@app.route('/confirm_loading_classroom', methods=['GET', 'POST'])
def confirm_loading_classroom():
    pass
