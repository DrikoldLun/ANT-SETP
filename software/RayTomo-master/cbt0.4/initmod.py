#!/usr/bin/env python
file='TEST_1_200_1000_25.1'
import numpy as np
from scipy.interpolate import griddata
lonb=97
lone=109
latb=20
late=30
v=3
lon=[]
lat=[]
vel=[]
'''
with open(file,'r') as f:
    for line in f.readlines():
        line=line.replace('\n','').split()
        lon.append(float(line[0]))
        lat.append(float(line[1]))
        vel.append(float(line[2]))
    f.close()
'''
lines=[]
for i in np.arange(-89,90,1):
    for j in np.arange(0,360,1):
        vel0=v
        '''
        if i<=late and i>=latb and j<=lone and j>=lonb:
            vel0=griddata(np.transpose(np.array([lon,lat])),np.array(vel),np.transpose(np.array([j,i])),method='nearest')[0]
        '''
        lines.append(str(j)+' '+str(i)+' '+str(vel0)+'\n')

with open('init.mod','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()
