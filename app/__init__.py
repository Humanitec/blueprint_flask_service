from flask import Flask
from app.config import config
from app.models import db, migrate
from app.resources import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(config[app.env or 'development'])
    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app)
    return app
