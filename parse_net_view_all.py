#!/usr/bin/env python

import sys

FILENAME = sys.argv[1]

f = open(FILENAME, "r")

raw_names = []
name_len = 0
for line in f:
    if line.find("Server Name") == 0:
        name_len = line.find("Remark")

    if line == "":
        continue
    
    if "-------------------------------------------------------------------------------" in line:
        continue

    if line == "The command completed successfully.":
        continue

    #line = line.strip()
    if len(line) > 80:
        raw_names.append(line[0:name_len].strip())

f.close()

outlist = ""
for name in raw_names:
    outlist += "\"%s\"," % name[2:]

print outlist[:-1]

    
