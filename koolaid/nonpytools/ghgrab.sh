#!/usr/local/bin/bash

###


if test -z "$1"
then
    echo "Supply a name or single word description of file"
    exit 1
else
    filename=$1
fi

########### CONSTANTS

GHURL="https://raw.github.com/lifeisstillgood/githubkoolaid/master/screenshots/"

IMGDIR="."

f_xwd=$IMGDIR/$filename.xwd
f_png=$IMGDIR/$filename.png

### Use alt-tab to get a clear view of the window to click on 
xwd -nobdrs -out $f_xwd
###
convert $f_xwd $f_png

echo "Shall we adjust $f_png in Gimp? [y/N] "
read usegimp

if [ "$usegimp"  == "y" ] || [ "$usegimp" == "Y" ]; 
then 
    gimp $f_png
else
    echo "..."
fi

echo "Uploading img to github, please wait"

cd $IMGDIR
git add  $f_png
git commit -m "Adding img $filename.png"
git push origin master

rm $IMGDIR/*.xwd

echo "paste this into ghi comment"
echo "\\![filename]($GHURL$filename.png)"
