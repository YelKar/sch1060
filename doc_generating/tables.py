from typing.io import IO

from app.database import Student
from openpyxl import Workbook


def generate(
        name: str | IO[bytes],
        dir_path: str = "",
        result_name="table.xlsx",
        result_dir_path: str = "",
        titles: list[str] = None,
        students: list[Student] = None
):
    if students is None:
        return None

    wb = Workbook()
    del wb["Sheet"]
