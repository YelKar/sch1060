import inspect
import os.path
import pythoncom
from win32com import client
from win32com.client import CDispatch


def convert(doc_path: str, result_doc_path: str = None):
    word = client.Dispatch("Word.Application", pythoncom.CoInitialize())
    if result_doc_path is None:
        result_doc_path = doc_path[:doc_path.rfind(".")] + ".pdf"

    doc: CDispatch = word.Documents.Open(os.path.abspath(doc_path))
    doc.SaveAs(os.path.abspath(result_doc_path), FileFormat=17)
    doc.Close()
    return result_doc_path


if __name__ == '__main__':
    convert("../app/static/documents/generated/Справка об обучении__16_03_2023__21-20-02.744654.docx")
