import datetime

from docx.opc.exceptions import PackageNotFoundError

from app import app
from app.database import Student, db
from docx import Document, document


with app.app_context():
    for st in Student.query.all():
        st: Student
        if st.classroom_letter < 500:
            st.classroom_letter = ord("НОПР"[st.classroom_letter])
    db.session.commit()
