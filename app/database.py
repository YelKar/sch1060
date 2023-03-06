from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32))
    lastname = db.Column(db.String(64))
    patronymic = db.Column(db.String(64))

    admission_year = db.Column(db.Integer())
    classroom_letter = db.Column(db.Integer())

    birthdate = db.Column(db.Integer())

    @property
    def grade(self):
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        current_grade = current_year - self.admission_year
        if current_month < 9:
            current_grade -= 1
        return current_grade

    @property
    def age(self):
        birthdate = datetime.fromtimestamp(self.birthdate).date()
        date = datetime.now().date()
        return date.year - birthdate.year - \
            (date.month < birthdate.month
             or date.day < birthdate.day)


class Info(db.Model):
    passport_series = db.Column(db.Integer())
    passport_number = db.Column(db.Integer())
    email: db.Column
    phone: db.Column


class Father(db.Model):
    pass


class Mother(db.Model):
    pass
