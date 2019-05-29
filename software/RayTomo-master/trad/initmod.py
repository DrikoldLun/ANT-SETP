#!/usr/bin/env python
import sys,getopt
def Usage():
    print('python initmod.py -Misinit(0,1) -Pprefix')
    sys.exit(1)

try:
    opts, args=getopt.getopt(sys.argv[1:],'M:P:')
except:
    print('Arguments are not found!')
    Usage()

if opts==[]:
    Usage()
for op,value in opts:
    if op=='-M':
        isinit=int(value)
        v=3
    elif op=='-P':
        prefix=value
    else:
        Usage()

if isinit == 0:
    file=prefix+'.1'
    prot=prefix+'.prot'
    with open(prot,'r') as f:
        a=f.readlines()
        f.close()
    v=float(a[-1].split()[3])
    lon=[]
    lat=[]
    vel=[]
    with open(file,'r') as f:
        for line in f.readlines():
            line=line.replace('\n','').split()
            lon.append(float(line[0]))
            lat.append(float(line[1]))
            vel.append(float(line[2]))
        f.close()

import numpy as np
from scipy.interpolate import griddata
lonb=97
lone=109
latb=20
late=30

lines=[]
for i in np.arange(-89,90,1):
    for j in np.arange(0,360,1):
        vel0=v
        if isinit==0 and i<=late and i>=latb and j<=lone and j>=lonb:
            vel0=griddata(np.transpose(np.array([lon,lat])),np.array(vel),np.transpose(np.array([j,i])),method='nearest')[0]
        lines.append(str(j)+' '+str(i)+' '+str(vel0)+'\n')

with open('init.mod','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()
