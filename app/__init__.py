from flask import Flask
from config import config
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


mongo = MongoEngine()
ma = Marshmallow()
jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mongo.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app