from flask import Flask
from .intents import intents


def create_app():

    app = Flask(__name__)
    app.register_blueprint(intents, url_prefix='/')

    return app