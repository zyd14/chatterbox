from typing import Dict

from marshmallow import Schema, fields, post_load

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

