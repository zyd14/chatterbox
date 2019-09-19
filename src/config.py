import json
import os
def get_token():
    if os.getenv('AWS_EXECUTION_ENV', None) or os.getenv('CI', None):
        token = os.getenv('SLACK_TOKEN')
    else:
        project_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
        with open(os.path.join(project_dir, 'chatterbox-remote-env.json'), 'r') as env:
            token = json.load(env)['SLACK_TOKEN']
    return token

class Config(object):
    DEBUG = False
    TESTING = False
    APP_NAME = 'TestingApp'
    SLACK_TOKEN = get_token()

class ChatterConfig(Config):
    pass

# CONFIG = {'APP_NAME': 'TestingApp',
#           'SLACK_TOKEN': get_token(),
#           'DEBUG': False,
#           'TEMPLATES_AUTO_RELOAD': False,
#           'SERVERNAME': 'localhost',
#           'APPLICATION_ROOT': '/'}

