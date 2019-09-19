import os

class Config(object):
    DEBUG = False
    TESTING = False

class ChatterConfig(Config):
    pass

CONFIG = {'APP_NAME': 'TestingApp',
          'SLACK_TOKEN': os.getenv('SLACK_TOKEN'),
          'DEBUG': False,
          'TEMPLATES_AUTO_RELOAD': False,
          'SERVERNAME': 'localhost',
          'APPLICATION_ROOT': '/'}

