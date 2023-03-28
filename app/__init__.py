from flask import Flask
from flask.templating import Environment

from app.util.config import Config
from app.util.constants import CONTEXT_CONSTANTS


app = Flask(__name__)
app.config.from_object(Config)
app.context_processor(lambda: CONTEXT_CONSTANTS)
app.jinja_env: Environment


from app.views import main
