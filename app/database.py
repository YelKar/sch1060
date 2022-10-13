from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from app import app


db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32))
    lastname = db.Column(db.String(64))
    patronymic = db.Column(db.String(64))

    admission_year = db.Column(db.Integer())
    classroom_letter = db.Column(db.Integer())

    birthdate = db.Column(db.Integer())

    def grade(self):
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        current_grade = current_year - self.admission_year
        if current_month < 9:
            current_grade -= 1
        return current_grade

    def old(self):
        birthdate = datetime.fromtimestamp(self.birthdate).date()
        date = datetime.now().date()
        return date.year - birthdate.year - \
               (date.month < birthdate.month
                or date.day < birthdate.day)
