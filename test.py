import datetime

from docx.opc.exceptions import PackageNotFoundError

from app import app
from app.database import Student, db
from docx import Document, document


with app.app_context():
    st = Student()
    st.__setattr__("name", "qwer")
    st.lastname = "KJHKHKHKJHKJH"
    st.patronymic = "JKHHJHK"
    db.session.add(st)
    db.session.commit()
