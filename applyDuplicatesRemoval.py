#!/usr/bin/env python3
import sys
import re

def getDuplicatesDict(filename):
    ret = dict()
    with open(filename, 'r') as inputfile:
        lines = inputfile.read().splitlines()
        marker = 0
        for line in lines:
            if line == '':
                marker = 0
            elif marker == 0 and line.startswith('# '):
                marker = 1
            elif marker == 1:
                newModule = line
                marker = 2
            elif marker == 2:
                ret[line] = newModule
    return ret

rmDup_txt = sys.argv[1]
input_cfg = sys.argv[2]
outpt_cfg = sys.argv[3]

dupDict = getDuplicatesDict(rmDup_txt)

with open(input_cfg, 'r') as ifile:
    ofile_str = ifile.read()
    for oldLabel, newLabel in dupDict.items():
        ofile_str = re.sub(rf'\b{oldLabel}\b', newLabel, ofile_str)

with open(outpt_cfg, 'w') as ofile:
    ofile.write(ofile_str)
