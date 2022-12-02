from flask import Flask

from app.config import Config
from app.constants import CONTEXT_CONSTANTS


app = Flask(__name__)
app.config.from_object(Config)
app.context_processor(lambda: CONTEXT_CONSTANTS)


from . import views
