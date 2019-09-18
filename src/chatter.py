import logging
from functools import wraps
import os
import ssl
from typing import Union

from flask import Response, make_response, jsonify
from flask_restful import Resource
from marshmallow import Schema
from werkzeug.local import LocalProxy

import slack

from src.setup_app import api
from src.exceptions import InvalidRequestStructureError
from src.requestschemas import SlackMessageSchema, SlackMessageModel

LOGGER = logging.getLogger('ChatterBox')
def fail_gracefully(func):
    """ Wrapper method to put a try/except block around the function passed by user which returns an HTTP 500 Internal Server Error
        response to the client when unhandled exceptions occur.  Should only be used in cases where a Response object is
        desired to be returned when an unhandled exception occurs.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Response:
        try:
            return func(*args, **kwargs)
        except BaseException as exc:
            if isinstance(exc, InvalidRequestStructureError):
                error_response = dict(message='InvalidRequestStructure',
                                      code=400,
                                      status='failure',
                                      errors=exc.errors)
            else:
                error_response = dict(message='Internal server error due to unhandled exception', error=str(exc),
                                      code=500,
                                      status='failure')
            LOGGER.exception(exc)
            return make_response(jsonify(**error_response), 500)

    return wrapper

class ChatterApi(Resource):

    @fail_gracefully
    @api.expect(SlackMessageModel)
    def post(self):
        from flask_restful import request

        LOGGER.info(f'Received request {request}')
        LOGGER.info(f'Request JSON data: {request.get_json()}')

        message_attrs = self.parse_request(SlackMessageSchema, request)

        token = os.getenv('SLACK_TOKEN')
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        slack_client = slack.WebClient(token=token,
                                       ssl=ssl_context)
        response = slack_client.chat_postMessage(**message_attrs)
        LOGGER.info(f'Slack client response: {response}')
        return make_response(jsonify(code=response.status_code, data=response.data), response.status_code)

    @staticmethod
    def parse_request(schema_type: type(Schema), request_in: Union[LocalProxy, dict]) -> dict:
        """ Use a marshmallow schema to parse JSON from a request or dict.  Will raise a InvalidRequestStructureError if any
            errors occur during parsing (such as missing or unexpected fields, wrong types).
        """
        schema = schema_type()

        if isinstance(request_in, LocalProxy):
            # Request originated externally.
            request_data = request_in.get_json(force=True)
            parsed_request = schema.load(request_data)
        else:
            # Request originated locally, probably from a test.
            parsed_request = schema.load(request_in)

        if parsed_request.errors:
            error_msg = 'Request is missing required keys or contains invalid value types.'
            raise InvalidRequestStructureError(error_msg, errors=parsed_request.errors)

        return parsed_request.data
