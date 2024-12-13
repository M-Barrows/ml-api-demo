from flask import Flask
from app.routes import main
import os

def create_app(config_class='config.Config'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config.from_pyfile('config.py', silent=True)

    app.register_blueprint(main)

    return app
