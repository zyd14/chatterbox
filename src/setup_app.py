from flask import Flask
from flask_restplus import Api

app = None
api = None

def setup_app_singleton():
    global app
    global api
    if not app or not api:
        app = Flask('compile-trigger')
        api = Api(app)
        return app, api
    else:
        return app, api

app, api = setup_app_singleton()