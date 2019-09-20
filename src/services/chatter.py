import ssl

import boto3
from flask import make_response, jsonify
from flask_restplus import Resource

import slack

from src.app import app, api
from src.services.requestschemas import SlackMessageSchema, SlackMessageModel, SlackCreateChannelSchema, SlackCreateSchemaModel
from src.utils import LOGGER, fail_gracefully, parse_request, httplog


def setup_slack_client(token: str):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    slack_client = slack.WebClient(token=token,
                                   ssl=ssl_context)
    return slack_client

slack_client = setup_slack_client(app.config['SLACK_TOKEN'])

class ChatterApi(Resource):

    @fail_gracefully
    @httplog
    @api.expect(SlackMessageModel)
    def post(self):
        from flask_restful import request
        message_attrs = parse_request(SlackMessageSchema, request)
        response = slack_client.chat_postMessage(**message_attrs)
        LOGGER.info(f'Slack client response: {response}')
        return make_response(jsonify(code=response.status_code, data=response.data), response.status_code)

class CreateChannel(Resource):

    @fail_gracefully
    @httplog
    @api.expect(SlackMessageModel)
    def post(self):
        from flask_restful import request
        message_attrs = parse_request(SlackCreateChannelSchema, request)
        response = slack_client.channels_create(**message_attrs)
        LOGGER.info(f'Slack client response: {response}')
        return make_response(jsonify(code=response.status_code, data=response.data), response.status_code)

def post_message_subscriber(message, context):
    pass

def message_to_db(message, context):
    client = boto3.client('dynamodb')
    channel = message['default']['channel']


