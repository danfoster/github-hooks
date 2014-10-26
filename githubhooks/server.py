#!/usr/bin/env python

from githubhooks.consumer import Consumer
from flask import Flask
from flask.ext import restful

def server():
    app = Flask(__name__)
    api = restful.Api(app)
    api.add_resource(Consumer, '/')
    app.run(host='0.0.0.0',debug=True)

if __name__ == '__main__':
    server()
