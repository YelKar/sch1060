from flask import Flask

from app.util.config import Config
from app.util.constants import CONTEXT_CONSTANTS


app = Flask(__name__)
app.config.from_object(Config)
app.context_processor(lambda: CONTEXT_CONSTANTS)


from app.views import main
