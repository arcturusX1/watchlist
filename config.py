import os

from model.model import db
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

api = Api()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ['URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']

def init_app(app):
    app.config.from_object(Config)

    migrate = Migrate()
    csrf = CSRFProtect()

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    api.init_app(app)
    CORS(app)

    with app.app_context():
        db.create_all()
    
    import logging
    logging.basicConfig(level=logging.DEBUG)

    return app