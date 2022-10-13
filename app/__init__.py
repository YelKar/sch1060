from flask import Flask

from app.config import Config

app = Flask()
app.config.from_object(Config)
app.context_processor(lambda: CONTEXT_CONSTANTS)



