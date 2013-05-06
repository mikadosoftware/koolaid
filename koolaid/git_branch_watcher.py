
"""
useage

  python git_branch_watcher.py /usr/path/myrepo branchname branchname2

Compares two git brnaches that are likely to share history and tries
to show which commits are in one and not the other.
It also make a good guess at cherry-picked commits

under the hood

DOnt look too closely - however sticks to sensible git work,
FIorstly the branch to branch compare is done via comparing rev SHA1 hashes
if same hash is in two branches, we can safely say they were the same
histry up to that point, so pass on.

I end up with two lists of commits - not-in-left and not-in-right which should sound obvious.

Then we use git patch-id to compare potential cherry picks, so we can elimate
some of the unshared commits as cherry picks.  git cherry does something similar and about 1000x as fast

issues

its slow, does loads of shelling out, loops over loops and... well it works ok


Why do this?

Partly to speed up repetitive git commands, partly to make a specific taks a abit clearer, plarty to understand more.

If git has plumbing and porcelain, this is at best the little yellow cube
in the urinal - it just makes it smell less.


Quick usage ::


1. git clone a repo into temp location
2. visit this files location

::

   >>> import git_branch_watcher
 
   >>> git_branch_watcher.get_all_branches_in_repo("/usr/home/pbrian/deploy/demo1/src/rhaptos2.repo")
   # This will vist the repo, and rather brutally, ensure each branch on remote
   # has a local mirror (makes the whole comparison feasible locally)

   >>> git_branch_watcher.prep_cmds("/usr/home/pbrian/deploy/demo1/src/rhaptos2.repo")
   # This will output a list of cmds that call *this* file with the
   # arguments of every branch in the above repo
   # ence we shall fill up a dir called "res" in this dir, with output
   # files listing what is / is not in Left and Right files
   
   
   >>> git_branch_watcher.dumb_method_of_checking_results("res")
   #this will output a cmpare of the results directory

"""
import subprocess
import sys
import os

def get_all_branches_in_repo(repo):
    """
    list all known, remote and local
    brnaches, munging into one local set, fully checked out and ready
    
    """
    cmd = "cd %s && git branch -a" 
    output = subprocess.check_output(cmd % repo, shell=True)
    allbranches = []
    for line in output.split("\n"):
        if line.strip() == "remotes/origin/HEAD -> origin/master": continue
        ll = line.strip().replace("*","")
        ll = ll.strip().replace("remotes/origin/","")
        ll = ll.strip()
        allbranches.append(ll)

    for br in set(allbranches):
        print "cd %s && git checkout %s && git pull origin %s && git checkout master" % (repo, br, br)
        
def prep_cmds(repo):
    """
    """
    cmd = "cd %s && git branch -a" 
    output = subprocess.check_output(cmd % repo, shell=True)
    allbranches = []
    for line in output.split("\n"):
        if line.strip() == "remotes/origin/HEAD -> origin/master": continue
        ll = line.strip().replace("*","")
        ll = ll.strip().replace("remotes/origin/","")
        ll = ll.strip()
        allbranches.append(ll)

    fo = open("br.sh", "w")    
    for br in set(allbranches):
        s = "python git_branch_watcher.py %s master %s > res/%s.res\n\n"
        fo.write(s % (repo, br, br))
    fo.close()

def dumb_method_of_checking_results(resdir):
    """
    look in resdir, check if last 
    """
    notinmaster = []
    inmaster = []
    files = [f for f in os.listdir(resdir) if f.find(".res")!=-1]
    for f in files:
        output = []
        flag = False
        for line in open(os.path.join(resdir, f)):
            if line.find("not in master") != -1:
                flag = True
            if flag:
                output.append(line)
        if len(output)>2:
            #we did find commits not in master
            notinmaster.append(f)
        else:
            inmaster.append(f)
            
    print "not in master", notinmaster
    print "*********"
    print "in master - deletable", inmaster
    

def acquire_rawlog_of_branch(repo, branch):
    """

    so far we ignore repo....
    """
    cmd = 'cd %s && git log --pretty=format:"%%H//%%ai//%%s" %s' % (repo, branch)
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
        firstslash = line.find("//")
        secondslash = line.find("//", firstslash+2)
        revhash = line[:firstslash]
        dt      = line[firstslash+2:secondslash]
        subject = line[secondslash+2:]
        
        orderlist.append(revhash)
        parsedlog[revhash] = [dt, subject]

    orderlist.reverse()
    return (orderlist, parsedlog)

def main(repo, leftbranch, rightbranch):
    """
    fixme: ensure ordering correct
    """
    
    leftorder, leftd =  acquire_parsedlog_of_branch(repo, leftbranch)
    rightorder, rightd = acquire_parsedlog_of_branch(repo, rightbranch)

    sleftorder = set(leftorder)
    srightorder = set(rightorder)

    notinright =  sleftorder - srightorder
    notinleft =  srightorder - sleftorder
    cherry_pairs = find_cherry(notinleft, notinright)
    
    #diverged at point
    #L ahead of R by
    #R ahead of L by
    print "Last common rev:"
    print "----------------"
    print "TBD"
    print
    print
    
    print "in %s not in %s" % (leftbranch, rightbranch)
    print "----------------"

    for revr in notinright:
        pairing = []
        for pair in cherry_pairs:
            if revr in pair:
                pairing = "<- %s paired with %s" % (pair[0][:8], pair[1][:8])                

        print revr[:8], leftd[revr][1], pairing
    print
    print
    
    #import pdb;pdb.set_trace()    
    print "in %s not in %s" % (rightbranch, leftbranch)
    print "----------------"

    for revl in notinleft:
        pairing = ''
        for pair in cherry_pairs:
            if revl in pair:
                pairing = "<- %s paired with %s" % (pair[0][:8], pair[1][:8])

        print revl[:8], rightd[revl][1], pairing
        
    
        
def find_cherry(notinleft, notinright):
    """
    Given two lists (or sets) of rev-hashes where
    they are rev not foundin the other branch,
    for each in each, compare to see if they are a cherry-pair
    """
    cherry_pairs = []
    for revl in notinleft:
        for revr in notinright:
            result = compare_patch_ids(repo, revl, revr)
            if result:
                cherry_pairs.append([revl, revr])
            else:
                pass
        
    for revr in notinright:
        for revl in notinleft:
            result = compare_patch_ids(repo, revr, revl)
            if result:
                cherry_pairs.append([revr, revl])
            else:
                pass

    
    return cherry_pairs
    

def compare_patch_ids(repo, revL, revR):
    """

    git patch-format

    181d9
    d93806

    probably want to use stringIO and similar
    
    """
    TMPDIR="/tmp"
    tmpL = os.path.join(TMPDIR, revL)
    tmpR = os.path.join(TMPDIR, revR)    
    
    cmd = "cd %s && git format-patch -1 --stdout %s > %s" 
    #tmpL
    subprocess.check_output(cmd % (repo, revL, tmpL),  shell=True)
    subprocess.check_output(cmd % (repo, revR, tmpR),  shell=True)    

    mkpatchid = "cd %s && git patch-id < %s" 
    patchidL =  subprocess.check_output(mkpatchid % (repo,tmpL),
                                                     shell=True)
    patchidR =  subprocess.check_output(mkpatchid % (repo, tmpR),
                                        shell=True)        

    leftid, leftrev = patchidL.split() 
    rightid, rightrev = patchidR.split()

    if leftid == rightid :
        return (leftrev, rightrev)
    else:
        return None
        
    
if __name__ == "__main__":
    repo = sys.argv[1:][0]
    leftbranch = sys.argv[1:][1]
    rightbranch = sys.argv[1:][2]

    help = """

      python git_branch_watcher.py /tmp/repo master dev-branch
    
    """
    main(repo, leftbranch, rightbranch)
    #compare_patch_ids('/usr/home/pbrian/src/public/Connexions/rhaptos2.repo',
    #                  '181d9','d93806')