import pip_helper

#print pip_helper.extract_imported_modules("/tmp/foo/foo.py")
#print pip_helper.find_imported_modules("/home/pbrian/src/public/Connexions/rhaptos2.repo")

#print pip_helper.discover_dependancies("Flask")
#print pip_helper.discover_dependancies("Jinja2")

reqfile = "requirements.txt"
list_of_pkgs =  pip_helper.parse_req(reqfile)
for pkg in list_of_pkgs:
    print "***"
    print pkg
    print pip_helper.discover_dependancies(pkg)
    print "***"
    