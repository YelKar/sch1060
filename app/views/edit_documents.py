import json
import os
from typing import Callable

from flask import render_template, request

from app import app
from app.util.constants import docs_path


@app.route('/edit_documents')
def edit_documents():
    return render_template("documents/edit_documents.html")


@app.route('/_edit_documents', methods=['POST'])
def _edit_documents():
    commands[request.form["command"]]()
    return "OK"


@app.route("/delete_document")
def delete_document():
    os.remove(os.path.join(docs_path, f"{request.form['document']}.docx"))


@app.route('/load_document', methods=['POST'])
def load_document():
    file = request.files["file"]
    file.save(os.path.join(docs_path, file.filename))
    return "Saved"


commands: dict[str, Callable] = {
    "delete": delete_document
}
