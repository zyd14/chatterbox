
from src.chatter import ChatterApi
from src.setup_app import app, api

def tie_resources():
    ns_message = api.namespace('message', 'Messaging operations')
    ns_message.add_resource(ChatterApi, '/slack')

tie_resources()

def run(debug: bool=False, host: str='0.0.0.0'):
    api.app.run(debug=debug, host=host)