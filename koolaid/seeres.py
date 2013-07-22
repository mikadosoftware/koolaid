import os

for file in os.listdir("res"):

    path = os.path.join("res", file)
    if path.find(".res") == -1: continue
    flag = False

    for line in open(path):
        if line.find("not in master") >0:
            flag = True
            print
            print file

        if flag: print line.replace("\n", "")

