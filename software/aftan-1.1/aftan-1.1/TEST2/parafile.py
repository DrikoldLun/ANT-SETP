#!/usr/bin/env python
import os
path='ANTdata/stack/'
lines=[]
for dir in os.listdir(path):
    for parent, dirnames, filenames in os.walk(path+dir):
        line='-1.0 1.5 5.0 4.0 40.0 20.0 1.0 1.0 0.2 1.0 '+path+dir+'/'+filenames[0]+'\n'
        lines.append(line)
with open('paratest1.dat','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()
