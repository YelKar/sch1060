from docx import Document
from flask import request, render_template, redirect, url_for
from werkzeug.datastructures import FileStorage

from app import app
from app.database import Student, db
from app.util.constants import class_letters
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


@app.route('/load_classroom', methods=["GET", "POST"])
def load_classroom():
    if request.form:
        file = request.files["input"]
        print(list(request.form.lists()))
        file.stream.seekable = lambda: True
        students = from_doc(file.stream, request.form["format"])
        return render_template("database/load_classroom.html", students=students)
    return redirect(url_for("database"))


@app.route('/confirm_loading_classroom', methods=['GET', 'POST'])
def load_classroom_to_db():
    students = {}
    admission_year = int(request.form["admission_year"])
    classroom_letter = class_letters.find(request.form["classroom_letter"].lower())

    assert classroom_letter != -1, "not specified classroom_letter"

    for key, val in request.form.items():
        if ":" in key:
            num, key = key.split(":")
            num = int(num)
            students[num] = students.get(num, {}) | {key: val}

    students_res = []
    for student in students.values():
        st = Student(admission_year=admission_year, classroom_letter=classroom_letter)
        for name, value in student.items():
            st.__setattr__(name, value)
        students_res.append(st)

    db.session.add_all(students_res)
    db.session.commit()
    return redirect(url_for("database"))
