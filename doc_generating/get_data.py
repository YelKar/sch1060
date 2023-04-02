import os
import re
from dataclasses import dataclass
from re import Pattern
from typing import Optional, Generator, Union, IO

from docx import Document
from docx.document import Document as DocType
from docx.text.paragraph import Paragraph


@dataclass
class Var:
    var: str
    dtype: str

    def __radd__(self, other):
        return other + self.var

    def __add__(self, other):
        return self.var + other

    def __str__(self):
        return self.var


format_vars = {
    "имя": Var("name", r"\w+"),
    "фамилия": Var("lastname", r"\w+"),
    "отчество": Var("patronymic", r"\w+"),
    "др": Var("birthdate_str", r"\d{2}\.\d{2}\.\d{4}")
}


def from_doc(doc_path: Union[str, os.PathLike, IO], format_: str) -> Generator[dict, None, None]:
    exp = compile_format(format_)
    doc: DocType = Document(doc_path)

    for par in doc.paragraphs:
        student = from_paragraph(par, exp)
        if student is None:
            continue
        yield student


def from_paragraph(par: Paragraph, exp: Pattern) -> Optional[dict]:
    result = exp.search(par.text)

    if result is None:
        return None
    return result.groupdict()


def compile_format(format_: str) -> Pattern:
    for k, v in format_vars.items():
        format_ = re.sub(
            re.compile(
                "// *" + k + " *//",
                flags=re.IGNORECASE
            ),
            "//"+v+"//",
            format_
        ).replace(
            "//"+v+"//",
            f"(?P<{v}>{v.dtype})"
        )
    return re.compile(format_.replace(" ", " +"), flags=re.IGNORECASE)


if __name__ == '__main__':
    print(
        *from_doc(
            "../file.docx",
            r"//фамилия// //имя// //отчество// //др//"
        ),
        sep="\n"
    )