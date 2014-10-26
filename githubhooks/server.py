#!/usr/bin/env python

import githubhooks
import githubevents
from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def consume_post():
    # Check for a valid github user-agent
    useragent = request.headers.get('User-Agent')
    if useragent == None or not useragent.startswith('GitHub-Hookshot'):
        print "ERROR: Incorrect client user-agent, rejecting request"
        return ""

    event = request.headers.get('X-GitHub-Event')
    if event == 'push':
        githubevents.push(request.data)
    return ""

def server():
    app.run(host='0.0.0.0',debug=False)

if __name__ == '__main__':
    server()
