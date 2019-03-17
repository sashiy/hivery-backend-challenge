from flask import Flask
from flask_bcrypt import Bcrypt

from .config import Config

flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    flask_bcrypt.init_app(app)

    return app
