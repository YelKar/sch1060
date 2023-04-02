from flask import Flask
from flask_login import LoginManager

from app.util.config import Config
from app.util.constants import CONTEXT_CONSTANTS


app = Flask(__name__)
app.config.from_object(Config)
app.context_processor(lambda: CONTEXT_CONSTANTS)

login_manager = LoginManager()
login_manager.init_app(app)


from app.views import main
