import logging
from logging import handlers
from functools import wraps
import json
from typing import Union

from flask import Response, make_response
from marshmallow import Schema
from werkzeug.local import LocalProxy

from src.exceptions import InvalidRequestStructureError

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
        except Exception as exc:
            if isinstance(exc, InvalidRequestStructureError):
                # Handle cases where request did not conform to a the required structure for that endpoint.
                code=400
                error_response = dict(message='InvalidRequestStructure',
                                      code=code,
                                      status='failure',
                                      errors=exc.errors)
            else:
                code = 500
                error_response = dict(message='Internal server error due to unhandled exception', error=str(exc),
                                      code=code,
                                      status='failure')
            LOGGER.exception(exc)
            return make_response(json.dumps(error_response), code)

    return wrapper

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

def httplog(func):
    from flask import request
    @wraps(func)
    def loghttp(*args, **kwargs):
        LOGGER.info(f'Incoming request: {request}')
        if request.method == 'POST':
            LOGGER.info(f'POST JSON data: {request.get_json()}')
        elif request.method == 'GET':
            LOGGER.info(f'GET query args: {request.args}')
        response = func(*args, **kwargs)
        LOGGER.info(f'{request.method} response: {response}')
        return response
    return loghttp

def create_logger(slack=True, file=False, config: dict=None):
    if slack:
        slack_handler = handlers.MemoryHandler(1, flushLevel=logging.INFO, target=SlackLogStreamer())
        LOGGER.addHandler(slack_handler)
    return LOGGER

class SlackLogStreamer:

    def handle(self, record):
        print(record)
        print(dir(record))
        self.send_slack_message(record)

    def send_slack_message(self, event):
        print(event)