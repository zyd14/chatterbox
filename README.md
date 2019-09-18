# Chatterbox

An alert service exposing REST endpoints for sending Slack messages

### Motivations
The purpose of this repository is to serve as practice for myself in building serverless REST APIs, as well as hopefully
serving as an example of one way these types of services can be implemented.  It is a work in progress and serves as both
an area of personal exploration, as well as hopefully a loose template that others may find useful when thinking about 
implementing their own APIs.  

The current implementation focuses on using the Flask microframework to provide a lightweight server which can handle HTTP
requests (GET / PATCH / POST ect.) to endpoints we make available in the application. There are a number of advantages to this
framework; the few I will list here include that it is lightweight but highly extentable, allowing you to install only the
functionality you need and keep your images small.  It is also well supported by a number of frameworks and tools which make
working in the cloud a much smoother experience, which is another focus of this repository.  

With regards to cloud infrastructure, this repository provides a deployment script configured for the [https://github.com/Miserlou/Zappa] (Zappa) deployment
framework, which enables seamless deployment of the Flask application onto AWS Lambda with an API Gateway proxy.  This means that 
with a single command you can turn your Flask application into an endpoint hosted in the cloud, reachable via HTTP and scalable to
tens of thousands of requests per second.

This repository also provides an example Circle CI configuration file.  This configuration allows for an automated build
of the application on a container on Circle CI's servers, running any specified tests before using the Zappa framework described
above to deploy the application to AWS, providing a seamless CI/CD pipeline that allows the developer to deliver new fixes and bug
patches in minutes.

Lastly this repository aims to provide a simple example in how to use the `flask-restplus` extension to provide beautiful Swagger
documentation for your RESTful interfaces.  Producing accurate Swagger documentation has saved me significant communication time
with consumers of my API, not to mention that it serves as a great reference for myself when I have a large API with lots of endpoints.  

In future iterations of this project I hope to explore more diverse implementations of similar concepts, such as 
- containerizing the application for deployments in Kubernetes clusters
- exploring the SAM framework for serverless AWS deployments
- Additional endpoints and interactions with persistent storage

## Chatterbox API

### Getting started
To download this package you can 
1. Clone from this repository

Option 1.  
From a terminal, type `git clone https://github.com/zyd14/chatterbox.git`  
The project will be downloaded into a subdirectory called 'chatterbox'.


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
