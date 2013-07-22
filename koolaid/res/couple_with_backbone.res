Last common rev:
----------------
TBD


in master not in couple_with_backbone
----------------
d8d8d4b6 Package dependancy fixes []
f69a4c51 make testuser independent of standalone server status []
7c27dd0e Manual (developer) installation instructions. []
618a0598 fix license header file []
ed705df0 kill off commented lines []
bcdda7ac need to return the mapper, and limit versions required []
7cf38279 add rhaptos2.user to install []
4457e0d2 Dbase field changes []
6031bbe2 Ensure we can fake the user header []
caf778c8 Changed the parameter name earlier, but didn't see it until now. []
46c586bd Added simple validity check to populate_self []
045085d1 Remove CNXEncoder class []
30111792 delete, not comment []
5789f65b Modifications to environment variables and how the configuration file is setup. This produces a configuration file that points to the location of the checked out ATC project. []
84ba9ad2 dump help to README.config as well as stdout []
abbe96fd Initialize the database using a 'rhaptos2repo-initdb' script that is created on installation of the package and points to rhaptos2.repo.run.initialize_database. []
3d1e9e44 Better explanation of the project. []
ed49eebc Merge branch 'master' into pseudomaster []
e0f71c59 Adjust checking of fake headersto avoid clash with session []
08988cb6 Aloha is pulled in as part of the external Authoring Tools Client (ATC) project, which is the javascript project that previously lived in this project. []
852b2df3 Add step for creating user DB into readme file []
c9d047e5 extend configto find local user server. Mention runnig user server in install script []
c4ebb975 Quick installation instructions revised to include the changes to the script. []
0340009a apply jsonify to all three models []
175f731d Standalone: allow URLMap to act as proxy []
7b46d546 Package dependancy fixes []
d6e457df Don't error on empty folders []
fa6e1cef Docs: Add extra documentation []
481bce87 Merge branch 'master' into license-and-docs []
a9e28ee3 Remove routing for static work from views []
2d6e9648 provide jsonable style encoding of an obnject at the object itself.  This commit expected to squash after a review and nights sleep []
97ad92c5 integrate restrest []
b4af3920 Dbase field changes []
ccc5d91a Merge branch 'master' into fake-user-header-in-wsgi []
371446e9 New configuration that removes any previously used configuration settings. []
77ecb6a3 redirect to match what atc now expects []
6a6410c8 Merge pull request #128 from zniper/update-readme []
db27c2eb Include the readme in the package's long-description, which can act as rst validation when using 'python setup.py --long-description | rst2html.py > description.html'. []
15e2eedc fix incorrect return of id only in folders. []
bf918d13 Added license info []
9f4f6668 allow system-site-packages, cut down requirements, and remove versions []
282bd6fa Initialize the ATC project after the clone. []
4278d7a9 Merge branch 'master' into test-user-switch []
7529d8f1 small code cleanup []
6a8ae1a6 Database init utility usage information. []
1c3fbf0b Merge pull request #102 from Connexions/demo_merge []
252cc53a Postgres installation information []
fdd2c55d Delete old dead folders []
70710a6f redirect index to atc page []
f8cff0a0 Fixes an RST syntax issue. []
35bb0d6a LICENSE: convert to AGPLv3 <- 35bb0d6a paired with d9c5567a
f1f537fa Unused setting... This persona setting was used in the templates to conditionally add persona support. []
4f7587f5 The commit notes idea was unnecessary []
c296332b Merge pull request #129 from Connexions/populate_self_robust []
1b251f0a put restrest in initially []
fc82f48f COnvert from jsonable name to __complex__ []
a69cd2cd make ini match code []
58c96309 Provides standalone server routing of static files from the ATC project. []
0e6ed336 replace long_description in setup []
58021226 Added license info []
aab83d02 Merge branch 'master' of github.com:Connexions/rhaptos2.repo []
1a8f513b Fix license header []
3149f51d Fix /js/ routing for dev server []
96714ef6 This setting is no longer used since we don't store anything on the filesystem. []
1ea625fb LICENSE: convert to AGPLv3 <- 1ea625fb paired with d9c5567a
bef9191a user and identity changes, ensuring consistent approach []
8b00d697 Save and Delete: make calls on object []
8d768574 Merge pull request #112 from Connexions/save-delete []
231ea9ff Dead file. This was once used to initialize configuration, but we no longer use environment variables. []
9e038d74 replace long_description in setup []
ee53d6b3 fixing merge issue with cherry-pick []
02abb602 make work again []
7d21e38e Docs: Add extra documentation []
452d65d8 Update README file with some missing items []
bbc5980e Save and Delete: make calls on object []
4562a1bf Restoring a set of useful default Postgres settings. []
7d6f89a3 Merge pull request #126 from Connexions/test-user-switch []
91032d24 If user has no permissions, return nothing []
4b7d3544 Docs: More doc changes, comments and logging. []
38fe177f pep8 []
dee8795b Better name for the setting since it just Aloha. []
1b0d3b2a merge two conflicting before_request methods []
8f7b2bd3 Dead file. []
f94fc76b adjust views to correctly append charset to response []
5dc64612 Zombie lines must die []
91f331e5 default to current dir, not users homedir []
23f9f8df Add softform parameters for the jsonify call []
a1afc258 Docs: More doc changes, comments and logging. []
bd1474ea Merge pull request #109 from Connexions/dbchanges []
a538ba4e Copy paste fix []
db4ab66e fix broken entrypoint []
c8cb85af zombie lines - this time more serious []
ff9980de Put back the session cookie setter. []
d93806ee Add in own HTTPException handling []


in couple_with_backbone not in master
----------------
4f2d127e Moving the resolution of pointer to object/json from backend to views 
590d0356 Minor bugfix - incorrect URN generated 
ff9ba790 Merge branch 'add_folders_to_backend' of github.com:Connexions/rhaptos2.repo into add_folders_to_backend 
daaa8276 use correct userURI to retrieve worksapce 
d9c5567a LICENSE AGPLv3 <- 1ea625fb paired with d9c5567a
efe2b6b5 branch for jasmine verification 
a95b71bb Allow logging in model and cnxbase. 
10b00e01 Remove extraneous assignment to older name of body 
e8c74d17 Revert "Matching demo on frozone" 
35791c05 Introduce HTTPException passing 
d9f7804b Improve api by having models call save and delete on themselves 
4b39e07b Added test for folder returning outputsuitable for backbone 
77f0c720 Remove unneeded static file serving 
f7c47a4d Always pass requiesting USer through to model for security check 
e06cc7da Matching demo on frozone 
f665ba61 fixed broken tests 
45f52148 Migrate the collections to use html snippets for holding collection 
f8030fd1 DOcs: improve flow of docs, kill off dead doc files. 
8c0e4ad3 fold various POST/PUT functions into resource specific if stmts 
c8d2cfcc migrated userroles to more meaningful date names 
db2d03a0 Fixing PEP8 
