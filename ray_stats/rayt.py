#!/usr/bin/env python
def Usage():
    print('python rayt.py -Tperiod -Cvphase')
import getopt
import sys
try:
    opts, args = getopt.getopt(sys.argv[1:], "T:C:")
except:
    print('Arguments are not found!')
    Usage()
    sys.exit(1)
if opts == []:
    Usage()
    sys.exit(1)
for op, value in opts:
    if op == "-T":
        T=float(value)
    elif op == "-C":
        c0=float(value)
    else:
        Usage()
        sys.exit(1)

import numpy as np
sta1=[]
sta2=[]
dist=[]
with open('distcut.lst','r') as f:
    lines=f.readlines()
    f.close()
for line in lines:
    sta1.append(line.split()[0])
    sta2.append(line.split()[1])
    dist.append(float(line.split()[2]))
dist=np.array(dist)
stalat={}
stalon={}
with open('../background/ANTcut.lst','r') as f:
    lines=f.readlines()
    f.close()
for line in lines:
    line=line.replace('\n','').split()
    stalat[line[0]]=float(line[1])
    stalon[line[0]]=float(line[2])

lines=[]
for i in range(len(dist)):
    if c0*T <= dist[i]/3: # and c0*T >= dist[i]/10:
        line=str(stalat[sta1[i]])+' '+str(stalon[sta1[i]])+' '+str(stalat[sta2[i]])+' '+str(stalon[sta2[i]])+' '+str(dist[i])+'\n'
        lines.append(line)

with open('rayt.dat','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()
