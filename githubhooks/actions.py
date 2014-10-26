import subprocess
import os

def gitpull(config):
    repodir =  os.path.expanduser(config['repodir']) 

    if not os.path.isdir(repodir):
        print "ERROR: no git repo found at %s" % repodir
        return

    with open(os.devnull, "w") as fnull:
        subprocess.Popen(['git','pull'],cwd=repodir,stdout=fnull,stderr=fnull)


