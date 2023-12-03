__version__ = '0.1.0'

from flask import Flask


def create_app():
    app = Flask(__name__)

    from .home import b_home
    app.register_blueprint(b_home)

    return app
