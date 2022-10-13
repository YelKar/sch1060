from datetime import datetime

CONTEXT_CONSTANTS = dict(
    base="base.html",
    about_site="School1060",
)


class_letters = "нопр"


def year_to_classroom(year):
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    classroom = current_year - year
    if current_month < 9:
        classroom -= 1
    return classroom
