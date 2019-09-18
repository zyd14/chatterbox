import json


class TestFailGracefully:

    def test_handles_bad_request(self, client_app):

        broken_data = {'channel': 123,
                       'username': 'brad',
                       'icon_emoji': ':kitty:',
                       'text': 'Hello'}

        result = client_app.post('/message/slack', data=json.dumps(broken_data), content_type='application/json')
        assert result.status_code == 400
