import pip_helper

#print pip_helper.extract_imported_modules("/tmp/foo/foo.py")





### python run_piphelper.py <requirements.txt> <toplevelpkgfolder>
import sys

reqfile = sys.argv[1:][0]
fldr = sys.argv[1:][1]

list_of_pkgs =  pip_helper.parse_req(reqfile)
s = ""
d = {}
all_pkgs = []
for pkg in list_of_pkgs:
    
    deps, srcpkgs =(pip_helper.discover_dependancies(pkg))
    all_pkgs.extend(deps)
    all_pkgs.extend(srcpkgs)
    
    for srcpkg in srcpkgs:
        for dep in deps:
            if dep == '' : continue
            if dep == None : continue            
        
            d.setdefault(srcpkg, []).append(dep)
line = "# %s provides the following\n"
for srcpkg in d:
    s += line % srcpkg
    for dep in d[srcpkg]:
        s+= "%s\n" % dep

print s


set_of_imported_modspkgs =  pip_helper.find_imported_modules(fldr)
set_all_pkgs = set(all_pkgs)

print "the following are in requirements but not seemingly impoprted"
print set_all_pkgs - set_of_imported_modspkgs

print "the following are in seemingly imported but not in req"
print set_of_imported_modspkgs - set_all_pkgs
