from docx.opc.exceptions import PackageNotFoundError

from app import app
from app.database import Student, db
from docx import Document, document


with app.app_context():
    for cr in range(10, 3, -1):
        for i, let in enumerate("НОП"):
            try:
                d: document.Document = Document(f"./Списки_классов/{cr} {let}.docx")
            except PackageNotFoundError:
                continue
            for par in d.paragraphs[2:-1]:
                fn = par.text.split()
                if not fn:
                    continue
                if fn[0] == "Карамышев":
                    continue
                s = Student(
                    name=fn[1].title(),
                    lastname=fn[0].title(),
                    patronymic=fn[2].title() if len(fn) >= 3 else None,
                    admission_year=2022 - cr,
                    classroom_letter=i
                )
                db.session.add(s)
                db.session.flush()
    db.session.commit()
