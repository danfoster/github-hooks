import json

def push(data):
    payload = json.loads(data)
    print json.dumps(payload, sort_keys=True,indent=4, separators=(',', ': '))
