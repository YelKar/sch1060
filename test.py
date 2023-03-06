from app.database import db, Student
from app import app
from app.util.constants import class_letters


with app.app_context():
    # for cl in range(5, 12):
    #     for let in range(4):
    #         for i in range(1, 11):
    #             s = Student(
    #                 name=f"N{cl}.{let}.{i}",
    #                 lastname=f"Ln{cl}.{let}.{i}",
    #                 patronymic=f"Patr{cl}.{let}.{i}",
    #                 admission_year=2023 - cl,
    #                 classroom_letter=let,
    #             )
    #             db.session.add(s)
    #         db.session.flush()
    # db.session.commit()
    print(
        Student.query
        .filter(Student.admission_year > 2015)
        .filter(Student.admission_year <= 2018)
        .filter_by(classroom_letter=3).delete()
    )
    db.session.commit()
