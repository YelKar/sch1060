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

    info = db.relationship("Info", backref="student", lazy=False)

    year_start_month = 9

    @property
    def birthdate(self):
        if self.birthdate_timestamp is None:
            return None
        date = datetime.fromtimestamp(self.birthdate_timestamp)
        return date

    @property
    def birthdate_str(self):
        if self.birthdate is None:
            return ""
        return self.birthdate.strftime("%d.%m.%Y")

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
    def letter(self):
        return class_letters[self.classroom_letter].upper()

    @property
    def age(self):
        if self.birthdate_timestamp is None:
            return None
        birthdate = datetime.fromtimestamp(self.birthdate_timestamp).date()
        date = datetime.now().date()
        return date.year - birthdate.year - \
            (date.month < birthdate.month
             or date.day < birthdate.day)

    @property
    def fullname(self):
        return " ".join(filter(None, (self.lastname, self.name, self.patronymic)))

    def to_dict(self):
        attrs = filter(lambda attr: not attr.startswith("_"), self.__dir__())
        return {attr: self.__getattribute__(attr) for attr in attrs}

    def __repr__(self):
        return f"<Student {self.id} {self.grade}{self.letter}>"


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
