#!/usr/bin/env python
import numpy as np
from scipy.interpolate import griddata

resofile='reso20s.dat'
cfile='TEST_0.1_200_1000_20.1'

lon0=[]
lat0=[]
reso0=[]

with open(resofile,'r') as f:
    for line in f.readlines():
        line=line.replace('\n','').split()
        lon0.append(float(line[3]))
        lat0.append(float(line[2]))
        reso0.append(float(line[4]))
    f.close()

lines=[]
with open(cfile,'r') as f:
    for line in f.readlines():
        line=line.replace('\n','').split()
        lon=float(line[0])
        lat=float(line[1])
        c=line[2]
        reso=griddata(np.transpose(np.array([lon0,lat0])),np.array(reso0),np.transpose(np.array([lon,lat])),method='cubic')
        if reso < 0.4:
            c=''
        lines.append(line[0]+' '+line[1]+' '+c+'\n')
    f.close()

with open('c20s.dat','w+') as f:
    f.writelines(lines)
    f.close()
