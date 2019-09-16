import attr
from typing import Dict

from marshmallow import Schema, fields, post_load

# class SlackMessage:
#     channel = attr.ib()  # type: str
#     username = attr.ib() # type: str
#     icon_emoji = attr.ib(default=None)  # type: str
#     blocks = attr.ib()  # type: dict
#     text = attr.ib()  # type: str

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

