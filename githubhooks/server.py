#!/usr/bin/env python

import githubhooks
import githubevents
import bitbucketevents
from flask import Flask, request
import config
import hmac, hashlib

app = Flask(__name__)

def _validate_sig(secret,sig):
    if not sig:
        print "ERROR: Secret configured but didn't recieve a signature from github. Aborting for safety"
        return False
    hash_name,hash = sig.split('=')
    if hash_name != 'sha1':
        return False

    h = hmac.new(str(config.config['secret']),digestmod=hashlib.sha1)
    h.update(request.data)
    f = h.hexdigest()
    return (hash == f)

@app.route('/',methods=['POST'])
def consume_post():
    # Check for a valid github user-agent
    useragent = request.headers.get('User-Agent')

    if useragent.startswith('GitHub-Hookshot'):
    	if "secret" in config.config:
            if not _validate_sig(config.config['secret'],request.headers.get('X-Hub-Signature')):
                print "ERROR: Could not validate github signature, aborting"
                return ""
        event = request.headers.get('X-GitHub-Event')
        if event == 'push':
            githubevents.push(request.data)
        return ""
    if useragent.startswith('Bitbucket-Webhooks'):
        event = request.headers.get('X-Event-Key')
	if event == 'repo:push':
            bitbucketevents.push(request.data)
	return ""
    else:
        print "ERROR: Incorrect client user-agent (%s), rejecting request"%useragent
        return ""




def server():
    app.debug = False
    app.run(host='0.0.0.0',port=int(config.config['port']))

if __name__ == '__main__':
    server()
