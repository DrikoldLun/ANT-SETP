#!/usr/bin/env python
import numpy as np
file = 'TEST_1_200_1000_20.1'
lines = ['c\n']
with open(file, 'r') as f:
    for line in f.readlines():
        line=line.split()
        lines.append(line[1]+' '+line[0]+'\n')
    f.close()

with open('SURF_POINTS', 'w+') as f:
    f.writelines(lines)
    f.close()


        
