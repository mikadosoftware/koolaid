#!/usr/bin/env python
#! -*- coding: utf-8 -*-

### Copyright Paul Brian 2013 

# This program is licensed, without  under the terms of the
# GNU General Public License version 2 (or later).  Please see
# LICENSE.txt for details

###

"""
:author:  paul@mikadosoftware.com <Paul Brian>


Cleaning up pip requirements.txt files is a pain.
However requirements files that import everything you ever installed
instead of the few files you meant annoys sysadmins.

Manually clean it up - no thanks, I take two bottles into the shower.

here we want to take a large requirements.txt file and produce a listing
of packages that are the top level, packages that are installed by
a top level, and packages that are not used by <some set of python modules>

.. todo::
   ignore -e lines
   

Future:
  Note when certain products are never called in files so
  not needed.
  grep import lines....

  for a file f
  import ast, _ast
  rootnode = ast.parse(open(f).read())
  for nd in ast.walk(rootnode):
      if isinstance(nd, _ast.Import):
          names = [mod.name for mod in nd.names] 
          
"""
import subprocess
import os
import ast, _ast

def extract_imported_modules(f):
    """
    parse the AST, grab import lines, and extract useful info
    THis is supposed to enable me to see what pkgs i am using in
    a folder/repo/pkg and so allow cleaning up of requirements file

    More work is needed to make it useful - its not clear if

      import foo

    imports a package (ie of interest) or a module
    Nor clear how to split

      import foo.bar

    or how to deal with

      from foo import bar
    
    """
    names = []
    rootnode = ast.parse(open(f).read())
    for nd in ast.walk(rootnode):
        if isinstance(nd, _ast.Import) or isinstance(nd, _ast.ImportFrom):
            names.extend([mod.name for mod in nd.names])
            if "module" in nd.__dict__.keys():
                names.extend([nd.module,])
    return names

def find_imported_modules(fldr):
    """
    """
    imports = []
    for root,dirs,files in os.walk(fldr):
        try:
            dirs.remove(".git");dirs.remove(".svn")
        except:
            pass
        pyfiles = [os.path.join(root,f)
                    for f in files
                     if os.path.splitext(f)[-1] == ".py"]
        for pyf in pyfiles:
            imports.extend(extract_imported_modules(pyf))
    return set(imports)
    
    
def parse_pip_line(l):
    """
    given a line like
    >>> L1 = "Requirement already satisfied (use --upgrade to upgrade): Jinja2 in /usr/home/pbrian/venvs/vscaffold/lib/python2.7/site-packages"
    >>> L2 = "Requirement already satisfied (use --upgrade to upgrade): Jinja2>=2.4 in /usr/home/pbrian/venvs/vscaffold/lib/python2.7/site-packages (from Flask)"
    >>> parse_pip_line(L1)
    ['Jinja2', None]
    >>> parse_pip_line(L2)
    ['Jinja2', 'Flask']
    
    """
    ### FIXME - this is brittle, do a regex
    sidx = l.find("):")
    eidx = l.find(" in ", sidx)
    pkg = l[sidx+2:eidx].strip()
    try:
        if pkg.find(">=") != -1:
            pkg = pkg[:pkg.find(">=")]
    except:
        pass
    ###
    sidx1 = l.find("(from")
    eidx1 = l.find(")", sidx1)
    if sidx1 == -1:
        srcpkg = None
    else:
        srcpkg = l[sidx1 + 5:eidx1].strip()    
    try:
        if srcpkg.find(">=") != -1:
            srcpkg = srcpkg[:srcpkg.find(">=")]
    except:
        pass
        
    return [pkg, srcpkg]


    
def discover_dependancies(pkgname):
    """
    """
    lprovide = []
    lsrcpkg = []
    try:
        cmd_output = subprocess.check_output(["pip", "install",
                                              "--no-install",
                               pkgname], shell=False,
                               stderr=subprocess.STDOUT)
    except Exception, e:
        raise e
        #FIXME - what action to take on err?
        
    for line in cmd_output.split("\n"):
        provides, srcpkg  = parse_pip_line(line)
        lprovide.append(provides)
        lsrcpkg.append(srcpkg)
    return ([i for i in set(lprovide)],
            [i for i in set(lsrcpkg)])
    

def parse_req(reqfile):
    """
    """
    all_pkgnames = []
    ignorelist = ["-e", "#"]    
    for line in open(reqfile):

        ##### ignore certain lines
        FLAG=False
        for i in ignorelist:
            if line.find(i) == 0 :
                FLAG=True
        if FLAG == True:
            print "ignored", line
            continue
        ##rather long winded///
        
        pkgname = line.split("=")[0]
        all_pkgnames.append(pkgname)
    return all_pkgnames


if __name__ == '__main__':
    #reqfile = sys.argv[1:][0]
    import doctest
    doctest.testmod()
    
