from datetime import datetime


CONTEXT_CONSTANTS = dict(
    base="bases/base.html",
    doc_base="bases/doc_base.html",
    select_students="bases/select_students.html",
    about_site="School1060",
    datetime=datetime,
    now=datetime.now,
    year_start_month=9
)

docs_path = "app/static/documents/templates"
result_docs_path = "app/static/documents/generated"

class_letters = "нопр"
