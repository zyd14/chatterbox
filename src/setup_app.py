from flask import Flask
from flask_restplus import Api

app = None
api = None

def setup_app_singleton():
    global app
    global api
    if not app or not api:
        from src.utils import create_logger
        app = Flask('compile-trigger')
        api = Api(app)
        app.logger = create_logger(slack=True)
        return app, api
    else:
        return app, api

app, api = setup_app_singleton()