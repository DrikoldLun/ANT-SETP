#!/usr/bin/env python
from scipy.interpolate import griddata
import numpy as np
lat0=[]
lon0=[]
ele0=[]
with open('../background/cut.dat','r') as f:
    for line in f.readlines():
        line=line.replace('\n','').split()
        lat0.append(float(line[1]))
        lon0.append(float(line[0]))
        ele0.append(float(line[2])/1000.)
        f.close()

ele0=np.array(ele0)
points0=np.transpose(np.array([lon0,lat0]))

stalst=[]
lat=[]
lon=[]
with open('../background/ANTcut.lst','r') as f:
    for line in f.readlines():
        line=line.replace('\n','').split()
        stalst.append(line[0])
        lat.append(float(line[1]))
        lon.append(float(line[2]))
        f.close()

point=np.transpose(np.array([lon,lat]))
ele=griddata(points0,ele0,point,method='nearest')
staele={}
for i in range(len(stalst)):
    staele[stalst[i]]=ele[i]

lines=[]
with open('dist.lst','r') as f:
    for line in f.readlines():
        sta1=line.split()[0]
        sta2=line.split()[1]
        if sta1 in stalst and sta2 in stalst:
            dist=float(line.split()[2])
            dist1=np.sqrt(dist**2+(staele[sta1]-staele[sta2])**2)
            line=sta1+' '+sta2+' '+str(dist)+' '+str(dist1)+'\n'
            lines.append(line)
    f.close()

with open('distcut.lst','w') as f:
    f.seek(0)
    f.writelines(lines)
    f.close()    
