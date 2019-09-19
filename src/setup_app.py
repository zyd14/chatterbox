from flask import Flask
from flask_restplus import Api

from src.utils import create_logger
from src.config import CONFIG


class AppSingleton:

    def __init__(self):
        self._app = None
        self._api = None
        self._setup_app_singleton()
    def _setup_app_singleton(self):
        if not self._app or not self._api:

            self._app = Flask(CONFIG['APP_NAME'])
            self._app.logger = create_logger(slack=True)
            self._app.config.from_object('src.config.ChatterConfig')
            self._api = Api(self._app)


    def get_app(self):
        return self._app

    def get_api(self):
        return self._api


sleepyapp = AppSingleton()