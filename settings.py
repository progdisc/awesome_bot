"""
Awesome Bot Settings
Mike Tung (seekheart)
"""

import json
import logging
import os


# setup logger format
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# setup configurations
ENV = os.environ.get('ENV', 'DEV')
CONFIG = os.environ.get('BOT_CONFIG', None)
CREDS = {}
with open(CONFIG, 'r') as c:
    c = json.load(c)
    CREDS['id'] = c['clientId']
    CREDS['secret'] = c['clientSecret']
    CREDS['token'] = c['token']
    PREFIX = c['botPrefix']

if ENV == 'PROD':
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.DEBUG)

