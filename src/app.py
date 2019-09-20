
from src.setup_app import sleepyapp
api = sleepyapp.get_api()
app = sleepyapp.get_app()

def tie_resources(api):
    from src.services.chatter import ChatterApi, CreateChannel
    ns_message = api.namespace('slack', 'Messaging operations')
    ns_message.add_resource(ChatterApi, '/message', endpoint='/slack/message')
    ns_message.add_resource(CreateChannel, '/create/channel', endpoint='/slack/create/channel')

tie_resources(api)

def run(debug: bool=False, host: str='0.0.0.0'):
    from src.setup_app import sleepyapp
    sleepyapp.get_api().app.run(debug=debug, host=host)


