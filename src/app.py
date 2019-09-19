
from src.setup_app import sleepyapp
api = sleepyapp.get_api()
app = sleepyapp.get_app()

def tie_resources(api):
    from src.services.chatter import ChatterApi
    ns_message = api.namespace('message', 'Messaging operations')
    ns_message.add_resource(ChatterApi, '/slack', endpoint='/message/slack')

tie_resources(api)

def run(debug: bool=False, host: str='0.0.0.0'):
    from src.setup_app import sleepyapp
    sleepyapp.get_api().app.run(debug=debug, host=host)


