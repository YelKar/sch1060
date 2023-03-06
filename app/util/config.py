import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "sfhlaeslvrlufgsgdafg"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../app/database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
