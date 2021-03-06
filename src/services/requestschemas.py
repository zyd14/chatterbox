from typing import Dict

from marshmallow import Schema, fields, post_load
from flask_restplus import Model, fields as api_fields

class SlackMessageSchema(Schema):
    channel = fields.String(required=True)
    username = fields.String(required=False, default='AutomatedAlert', missing='AutomatedAlert')
    icon_emoji = fields.String(required=False)
    blocks = fields.List(fields.Dict(), required=False)
    text = fields.String(required=True)

    @post_load()
    def cleanup(self, data: Dict[str, str]):
        data['channel'] = data['channel'].strip()
        data['username'] = data['username'].strip()
        return data

class SlackMessageModel(Model):
    channel = api_fields.String(required=True)
    username = api_fields.String(required=False)
    icon_emoji = api_fields.String(required=False)
    blocks = api_fields.List(api_fields.Raw(), required=False)
    text = api_fields.String(required=True)