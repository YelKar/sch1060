from os import listdir

from app.util.constants import docs_path


def get_documents():
    return listdir(docs_path)
