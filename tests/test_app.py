import json

def test_nothing(client_app):
    test_request = {"channel": "#errors",
     "username": "KevinAlerts",
     "icon_emoji": ":kevin_scream:",
     "text": "Dont panic, this is just a test",
     "blocks": [{"type": "section",
                 "text": {"type": "plain_text",
                          "text": "just another test"}
                 }]}
    response = client_app.post('/message/slack', data=json.dumps(test_request))
    assert response.status_code == 200