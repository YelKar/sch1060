from typing import Union, Any

from flask import request, render_template, redirect, url_for

from app import app
from app.database import Student, db
from doc_generating.get_data import from_doc


@app.route('/database')
def database():
    return render_template(
        "database/database.html",
        editable_fields=Student.editable_fields
    )


@app.route('/delete_students', methods=["POST"])
def delete_students():
    *ids, = map(int, bytes(request.data).decode().split(","))
    Student.query.filter(Student.id.in_(ids)).delete()
    db.session.commit()
    return "OK"


@app.route('/add_student', methods=["POST"])
def add_student():
    form = dict(request.form)
    res = add_students(int(form.pop("admission_year")), form, letter=form.pop("letter"))
    db.session.add_all(res)
    db.session.commit()
    return "OK"


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
    classroom_letter = request.form["classroom_letter"]

    for key, val in request.form.items():
        if ":" in key:
            num, key = key.split(":")
            num = int(num)
            students[num] = students.get(num, {}) | {key: val}

    students_res = add_students(admission_year, *students.values(), letter=classroom_letter)

    db.session.add_all(students_res)
    db.session.commit()
    return redirect(url_for("database"))


def add_students(
        admission_year: int,
        *students: dict[str, Any],
        classroom_letter: Union[str, int] = None,
        letter: str = None,
):
    for student in students:
        st = Student(admission_year=admission_year, letter=letter, classroom_letter=classroom_letter)
        for name, value in student.items():
            st.__setattr__(name, value)
        yield st
