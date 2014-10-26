import os.path
import sys
import json


def parseconfig():
    stream = open(_findconfigfile(), 'r')
    return json.load(stream)


def _findconfigfile():
    """
    Find a valid config file to load on the filesystem
    """

    # A ordered list of possible config files
    configfiles = ["~/.githubhooksrc",
                   "/etc/githubhooks"]

    for configfile in configfiles:
        if os.path.isfile(os.path.expanduser(configfile)):
            return os.path.expanduser(configfile)

    # No valid config file found
    print "ERROR: No valid config file found in any of the following locations:"
    for configfile in configfiles:
        print " - %s" % configfile
    sys.exit(1)

config = parseconfig()
