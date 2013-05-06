"""
measure if remote refs and local refs out of step.
Probably a better way.
"""
import sys, os

dotgit = sys.argv[1:][0]
headsdir = os.path.join(dotgit, 'refs', 'heads')
remotesdir = os.path.join(dotgit, 'refs', 'remotes', 'origin')

for branchname in os.listdir(headsdir):
    print branchname + ":: ",
    revhead = open(os.path.join(headsdir, branchname)).read()
    try:
        revremote = open(os.path.join(remotesdir, branchname)).read()
    except IOError:
        print "no remote branch" 
        continue
    if revhead == revremote:
        print "matches"
    else:
        print "error", revhead, revremote

        
    
