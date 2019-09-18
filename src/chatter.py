import logging
from functools import wraps
import json
import os
import ssl
from typing import Union

from flask import make_response, jsonify
from flask_restplus import Resource

import slack

from src.setup_app import api
from src.requestschemas import SlackMessageSchema, SlackMessageModel
from src.utils import LOGGER, fail_gracefully, parse_request


class ChatterApi(Resource):

    @fail_gracefully
    @api.expect(SlackMessageModel(name='slackmessage'))
    def post(self):
        from flask_restful import request

        LOGGER.info(f'Received request {request}')
        LOGGER.info(f'Request JSON data: {request.get_json()}')

        message_attrs = parse_request(SlackMessageSchema, request)

        token = self.get_token()
        slack_client = self.setup_slack_client(token)
        response = slack_client.chat_postMessage(**message_attrs)
        LOGGER.info(f'Slack client response: {response}')
        return make_response(jsonify(code=response.status_code, data=response.data), response.status_code)

    @staticmethod
    def get_token() -> str:
        if os.getenv('AWS_EXECUTION_ENV', None) or os.getenv('CI', None):
            token = os.getenv('SLACK_TOKEN')
        else:
            project_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
            with open(os.path.join(project_dir, 'chatterbox-remote-env.json'), 'r') as env:
                token = json.load(env)['SLACK_TOKEN']
        return token

    @staticmethod
    def setup_slack_client(token: str):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        slack_client = slack.WebClient(token=token,
                                       ssl=ssl_context)
        return slack_client

