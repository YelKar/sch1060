from os import path
from typing import IO

import docxtpl
from doc_generating.context import Context


def generate(
        doc: str | IO[bytes],
        dir_path: str = "",
        result_doc_name="rendered_file.docx",
        result_dir_path: str = "", **context
):
    """Generate document
    Get document template <doc_name> from <dir_path> folder
    Pass context variables for jinja to template
    Save result document <result_doc_name>
        to <result_dir_path> if it was specified
        else used <dir_path>

    :param doc: .docx template name
    :param dir_path: path to template
    :param result_doc_name: name of generated document
    :param result_dir_path: save path for document
    :param context: jinja variables
    :return:
    """
    assert isinstance(doc, str | IO), "passed wrong value. Parameter doc must be string or IO"

    result_dir_path = result_dir_path or dir_path
    doc_path = path.join(dir_path, doc)
    result_doc_path = path.join(result_dir_path, result_doc_name)
    ctx = Context(context)

    doc = docxtpl.DocxTemplate(f"{doc_path}.docx")
    doc.render(ctx)
    doc.save(result_doc_path)
    return result_doc_path


if __name__ == '__main__':
    pass
