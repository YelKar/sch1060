import sys

from flask import request
from loguru import logger

sending_text_color = "fg #85a7ff"


class C:
    @staticmethod
    def __getitem__(item):
        return dir(item), type(item)


logger.configure(
    handlers=[
        dict(sink=sys.stderr,
             format=(
                 '{extra[request].remote_addr} - - '
                 '[{time:DD/MMM/YYYY HH:mm:ss}] '
                 f'"<{sending_text_color}>'
                 '{extra[request].method} {extra[request].path} '
                 '{extra[request].environ[SERVER_PROTOCOL]}" '
                 '{level} - {message}'
                 f'</{sending_text_color}>"'
             ))
    ],
    levels=[dict(name="FILE SENDING", no=10, color="<green>")],
    extra=dict(request=request)
)

logger.log("FILE SENDING", "Hello")
