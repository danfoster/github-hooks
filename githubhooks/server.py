#!/usr/bin/env python

import githubhooks
from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def consume_post():
    useragent = request.headers.get('User-Agent')
    if useragent == None or not useragent.startswith('GitHub-Hookshot'):
        print "ERROR: Incorrect client user-agent, rejecting request"
        return ""
    return ""

def server():
    app.run(host='0.0.0.0',debug=True)

if __name__ == '__main__':
    server()
