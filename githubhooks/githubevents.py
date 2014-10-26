import json
import config
import actions

def push(data):
    payload = json.loads(data)
    full_name = payload['repository']['full_name']
    if full_name not in config.config['repos']:
        print "ERROR: %s is an unconfigured repo, please add an entry to the config if you want to trigger on it" % (full_name)
        return
    repoconfig = config.config['repos'][full_name]
    branch = payload['ref']
    
    if branch not in repoconfig:
        print "ERROR: %s is an unconfigured branch under the %s repo, please add an entry to the config if you want to trigger on it" % (branch, full_name)
        return

    branchconfig = repoconfig[branch]

    if hasattr(actions,branchconfig['action']):
        getattr(actions,branchconfig['action'])(branchconfig)
    else:
        print "ERROR: Unknown action %s" % branchconfig['action']
        return
