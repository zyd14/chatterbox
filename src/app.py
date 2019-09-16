import os

from flask import Flask
from flask_restful import Api

from src.chatter import ChatterApi

_app = None
_api = None

def _setup_app(app, api):
    if not app or not api:
        app = Flask('compile-trigger')

        # Add AWS X-Ray if program is run from AWS and not from CircleCi
        if not os.getenv('CI', None) and os.getenv('AWS_EXECUTION_ENV', None):
            from aws_xray_sdk.core import xray_recorder, patch_all
            from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
            xray_recorder.configure(service='compile-trigger')
            XRayMiddleware(app, xray_recorder)
            patch_all()

        api = Api(app)

        api.add_resource(ChatterApi, '/message/slack')
        return app, api

app, api = _setup_app(_app, _api)