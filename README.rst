:desc: managing a git repo - tools and tricks

============================
Useful Github related tricks
============================

ghi
===

Immensiely useful commandline tool 
Setting up for non-rubyists is a bit painful

1. Install ruby (1.8 is fine, 1.9 should be good too)
2. install gems 
3. check what the header directory is for compilation 
4. run the below

   sudo /usr/local/bin/gem18 install iconv -- --with-opt-dir=/usr/local/

5. sudo /usr/local/bin/gem18 install ghi

6. ghi will walk you thorugh obtaining a token for access on first commit attempt


Screenshots in issues
=====================

OK, we create an issues as ::

    ghi open -m "The foobar is wrong colour"

How do we add an image?::


    ghgrab.sh foobarcolour

(FreeBSD tested- any other unixes let me know)
This will fire :cmd:`xwd` which you use to select a window,
that window snapshot will be written to :dir:`screenshots`
in this repo. And uploaded on master branch.
And then the URL to refer to it in an issue provided




