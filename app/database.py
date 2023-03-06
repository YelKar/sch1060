from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from app import app
from app.util.constants import class_letters

db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(32))
    lastname = db.Column(db.String(64))
    patronymic = db.Column(db.String(64))

    admission_year = db.Column(db.Integer())
    classroom_letter = db.Column(db.Integer())

    birthdate_timestamp = db.Column(db.Integer())

    info = db.relationship("Info", backref="student")

    year_start_month = 9

    @property
    def birthdate(self):
        date = datetime.fromtimestamp(self.birthdate_timestamp)
        return date.strftime("%d.%m.%Y")

    @property
    def grade(self):
        now = datetime.now().date()
        current_year = now.year
        current_month = now.month
        current_grade = current_year - self.admission_year
        if current_month >= self.year_start_month:
            current_grade += 1
        return current_grade

    @property
    def age(self):
        birthdate = datetime.fromtimestamp(self.birthdate_timestamp).date()
        date = datetime.now().date()
        return date.year - birthdate.year - \
            (date.month < birthdate.month
             or date.day < birthdate.day)

    @property
    def fullname(self):
        return " ".join((self.lastname, self.name, self.patronymic))

    #
    # @classmethod
    # def to_dict(cls):
    #     pass

    def __repr__(self):
        return f"<Student {self.id} {self.grade}{class_letters[self.classroom_letter]}>"


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey("student.id"))

    email = db.Column(db.String(128))
    phone = db.Column(db.Integer())

    home_phone = db.Column(db.String(32))
    address = db.Column(db.String(256))
    parent_emails = db.Column(db.PickleType())

    birth_certificate = db.Column(db.String(32))

    passport_series = db.Column(db.Integer())
    passport_number = db.Column(db.Integer())

#
# class Father(db.Model):
#     pass
#
#
# class Mother(db.Model):
#     pass


if __name__ == '__main__':
    db.create_all()
