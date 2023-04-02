from datetime import datetime
from typing import Optional

from flask_sqlalchemy import SQLAlchemy

from app import app
from app.util.constants import CONTEXT_CONSTANTS


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

    year_start_month = CONTEXT_CONSTANTS["year_start_month"]

    editable_fields = {
        "lastname": "фамилия",
        "name": "имя",
        "patronymic": "отчество",
        "grade": "класс",
        "letter": "буква",
        "birthdate_str": "дата рождения"
    }

    birthdate_format = "%d.%m.%Y"

    @classmethod
    def grade_to_admission_year(cls, grade):
        pass

    @property
    def birthdate(self) -> Optional[datetime]:
        if self.birthdate_timestamp is None:
            return None
        date = datetime.fromtimestamp(self.birthdate_timestamp)
        return date

    @birthdate.setter
    def birthdate(self, birthdate: datetime):
        self.birthdate_timestamp = birthdate.timestamp()

    @property
    def birthdate_str(self):
        if self.birthdate is None:
            return ""
        return self.birthdate.strftime(self.birthdate_format)

    @birthdate_str.setter
    def birthdate_str(self, date_string: str):
        self.birthdate = datetime.strptime(date_string, self.birthdate_format)

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
        return chr(self.classroom_letter).upper()

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
