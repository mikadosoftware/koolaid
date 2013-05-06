f = '/tmp/branches'
for line in open(f):
    br = line.replace("*","").strip()

    cmd = 'python git_branch_watcher.py /usr/home/pbrian/src/public/Connexions/rhaptos2.repo/rhaptos2/repo master %s > %s.res'

    print cmd % (br, br)