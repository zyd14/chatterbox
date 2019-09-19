import ssl

import boto3
from flask import make_response, jsonify
from flask_restplus import Resource

import slack

from src.app import app, api
from src.services.requestschemas import SlackMessageSchema, SlackMessageModel
from src.utils import LOGGER, fail_gracefully, parse_request, httplog

class ChatterApi(Resource):

    @fail_gracefully
    @httplog
    @api.expect(SlackMessageModel(name='slackmessage'))
    def post(self):
        from flask_restful import request

        LOGGER.info(f'Received request {request}')
        LOGGER.info(f'Request JSON data: {request.get_json()}')

        message_attrs = parse_request(SlackMessageSchema, request)

        slack_client = self.setup_slack_client(app.config['SLACK_TOKEN'])
        response = slack_client.chat_postMessage(**message_attrs)
        LOGGER.info(f'Slack client response: {response}')
        return make_response(jsonify(code=response.status_code, data=response.data), response.status_code)

    @staticmethod
    def setup_slack_client(token: str):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        slack_client = slack.WebClient(token=token,
                                       ssl=ssl_context)
        return slack_client

def message_to_db(message, context):
    client = boto3.client('dynamodb')
    channel = message['default']['channel']


