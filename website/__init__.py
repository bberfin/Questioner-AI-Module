from flask import Flask
from .intents import intents


def create_app():

    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.register_blueprint(intents, url_prefix='/')

    return app