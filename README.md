# Chatterbox

An alert service exposing REST endpoints for sending Slack messages

### AWS-hosted deployment endpoints:
| Deployment Stage | Endpoint URL |
| :---:  | --- |
| Production | https://80oamlb410.execute-api.us-west-2.amazonaws.com/production/message/slack

### Request Structure:

#### /message/slack
Headers: `["Content-Type: application/json"]`
HTTP request type: POST
Payload:
```json
{
"channel": "[REQUIRED] <str> - Slack channel to send message to",
"username": "[REQUIRED] <str> - Username to send message from",
"icon_emoji": "[OPTIONAL] <str> - Emoji tag to append to message (e.g. :kevin_scream:)",
"blocks": "[OPTIONAL] <list> - list of dictionaries describing text blocks making up more complex messages",
"text": "[REQUIRED] <str> - text to put in message if blocks are not used."
}
```  
An example request can be found in the root of the project folder, labeled `chatterbox-test-request.json`.  An example curl command
using this request would be:  
`curl -X POST -d @chatterbox-test-request.json https://80oamlb410.execute-api.us-west-2.amazonaws.com/production/message/slack`   
