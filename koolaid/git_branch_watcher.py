
"""

"""
import subprocess

def acquire_rawlog_of_branch(repo, branch):
    """
    """
    cmd = 'git log --pretty=format:"%H//%ai//%s"'
    output = subprocess.check_output(cmd, shell=True)
    return output
    
def acquire_parsedlog_of_branch(repo, branch):
    """
    """
    parsedlog = {}
    orderlist = []
    rawlog = acquire_rawlog_of_branch(repo, branch)
    for line in rawlog.split("\n"):
        ##fixme - if // in subject line?
        revhash, dt, subject = line.split("//")
        orderlist.append(revhash)
        parsedlog[revhash] = [dt, subject]

    orderlist.reverse()
    return (orderlist, parsedlog)

print acquire_parsedlog_of_branch(None, None)